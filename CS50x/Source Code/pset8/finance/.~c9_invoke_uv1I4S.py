import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")

globalCounter = 0

@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    # Get user's id from session
    user_id = session["user_id"]

    # Query db for user's cash
    cash = db.execute("SELECT cash from users WHERE id= :user_id", user_id=user_id)

    # dataBase = db.execute("SELECT type, name, symbol, qty FROM purchase UNION SELECT type, name, symbol, qty FROM sell WHERE user_id=:user_id AND GROUP BY symbol ORDER BY name")
    # dataBase = db.execute("SELECT name, symbol, SUM(qty) FROM purchase WHERE user_id=:user_id GROUP BY symbol", user_id=user_id)
    # dataBase = db.execute("SELECT purchase.name, purchase.symbol, stocks.totalQty FROM purchase JOIN stocks ON purchase.user_id=stocks.user_id GROUP BY purchase.symbol")

    # Query db for purchase table
    dataBase = db.execute("SELECT name, symbol, SUM(qty) FROM purchase WHERE user_id=:user_id GROUP BY symbol HAVING SUM(qty) > 0", user_id=user_id)

    # Declare counter variables
    totalCounter = 0

    for data in dataBase:
        # pass in each symbol into lookup function, returns dict info (name, symbol, price)
        stock_info = lookup(data["symbol"])

        # add actual price of stock to list of dicts
        data["price"] = stock_info["price"]

        # add total value (actual price * owned shares) to list of dicts
        data["totalValue"] = stock_info["price"]  * data["SUM(qty)"]

        totalCounter += data["totalValue"]

    return render_template("index.html", cash=cash, totalCounter=totalCounter, dataBase=dataBase)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    # POST
    if request.method == "POST":

        # Variables
        # Get user's id from session
        user_id = session["user_id"]

        # API stock info
        stock_info = lookup(request.form.get("symbol"))

        # N of shares
        shares = int(request.form.get("shares"))

        # Buying price
        total = shares * stock_info["price"]

         # Query db for user's cash
        cash = db.execute("SELECT cash FROM users WHERE id=:user_id", user_id=user_id)

        # Balance after BUY
        balance = cash[0]["cash"] - total

        # Data validation
        try:
            # Check. Enter input stock_info
            if not request.form.get("symbol"):
                return apology("You must enter a stock symbol", 403)

            # Check. If input exists in API query
            elif stock_info == None:
                return apology("This stock symbol doesn't exist.", 403)

            # Check Enter input shares
            elif not shares:
                return apology("You must enter the number of shares you want to buy", 403)

            # Check. Input shares must be greater than one.
            elif shares < 1:
                return apology("You must buy at least 1 stock", 403)

            # Check if enough credits
            elif balance < 0:
                return apology("You don't have enough credits", 403)

            # Correct data validation: BUY.
            else:
                # Tracking purchase
                db.execute("INSERT INTO purchase (user_id, name, symbol, qty, price) VALUES (:user_id, :name, :symbol, :qty, :price)", user_id=user_id, name=stock_info["name"], symbol=stock_info["symbol"], qty=shares, price=stock_info["price"])

                # Update $ cash
                db.execute("UPDATE users SET cash=:cash WHERE id=:user_id", cash=balance, user_id=user_id)

                return redirect("/")
        # Data validation: value not an integer.
        except ValueError:
            return apology("You must enter an integer", 403)
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    #dataBase = db.execute("SELECT type, name, symbol, qty, price, timestamp FROM purchase UNION SELECT type, name, symbol, qty, price, timestamp FROM sell ORDER BY timestamp")
    dataBase = db.execute("SELECT type, name, symbol, qty, price, timestamp FROM purchase ORDER BY timestamp")
    return render_template("history.html", dataBase=dataBase)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        # Manage lookup == None
        symbol = lookup(request.form.get("symbol"))
        return render_template("quoted.html", symbol=symbol)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        if not request.form.get("username"):
            return apology("must provide username", 403)

        elif request.form.get("username") == db.execute("SELECT * FROM users"):
            return apology("that username already exists", 403)

        elif not request.form.get("password") or not request.form.get("confirmation"):
            return apology("must fill all password fields", 403)

        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("password and confirmation don't match!", 403)

        else:
            username = request.form.get("username")
            hashPassword = generate_password_hash(request.form.get("password"))
            db.execute("INSERT INTO users (username, hash) VALUES (:username, :password)", username=username, password=hashPassword)
            return redirect("/")
    else:
    # User reached route via GET (as by clicking a link or via redirect)
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    # Get user's id from session
    user_id = session["user_id"]

    # POST
    if request.method == "POST":

        # Variables
        # API stock info
        stock_info = lookup(request.form.get("symbol"))

        # N of shares trying to sell
        shares = int(request.form.get("shares"))

        # Selling price
        total = shares * stock_info["price"]

        # Query db for user's cash
        cash = db.execute("SELECT cash FROM users WHERE id=:user_id", user_id=user_id)

        # Balance after SELL
        balance = cash[0]["cash"] + total

        # TODO
        # Query db for N of shares of particular stock
        dataBase = db.execute("SELECT name, symbol, SUM(qty) FROM purchase WHERE user_id=:user_id", user_id=user_id)

        # N of shares owned
        owned = dataBase[0]["SUM(qty)"]

        # Data validation
        try:
            # Check. Enter input stock_info
            if not request.form.get("symbol"):
                return apology("You must choose a stock symbol", 403)

            # # Check. Enter input shares
            if not shares:
                return apology("You must enter the number of shares you want to sell", 403)

            # verify entered a positive integer
            if shares < 1:
                return apology("You must sell at least 1 stock", 403)

            #CHECK VERIFICATION
            # Check if stock not found
            if len(dataBase) != 1:
                return apology("You don't own any of this particular stock!", 403)

            # Check. if stock found.
            if len(dataBase) == 1:

                #Check. if enough shares to sell
                if owned < shares:
                    return apology("You're trying to sell more stocks than you have!", 403)

                # Correct data validation: SELL.
                else:
                    # Tracking selling stocks
                    shares = shares * -1
                    db.execute("INSERT INTO purchase (user_id, name, symbol, qty, price, type) VALUES (:user_id, :name, :symbol, :qty, :price, :type)", user_id=user_id, name=stock_info["name"], symbol=stock_info["symbol"], qty=shares, price=stock_info["price"], type=["sell"])

                    # Update $ database
                    db.execute("UPDATE users SET cash= :balance WHERE id= :user_id", balance=balance, user_id=user_id)
                    # db.execute("UPDATE stocks SET totalQty= :totalQty WHERE id= :user_id AND symbol= :symbol", totalQty=qty, user_id=user_id, symbol=symbol["symbol"])
                    return redirect("/")

        # Data validation
        except ValueError:
            return apology("You must enter an integer", 403)
    # GET
    else:
        # Dropdown. Owned symbols to sell
        symbols = db.execute("SELECT symbol FROM purchase WHERE user_id= :user_id GROUP BY symbol HAVING SUM(qty) > 0", user_id=user_id)
        return render_template("sell.html", symbols=symbols)


@app.route("/changepwd", methods=["GET", "POST"])
@login_required
def change_pwd():
    """Change password"""

    if request.method == "POST":
        # Get user's id from session
        user_id = session["user_id"]

        # Inputs
        pwdOld = request.form.get("password")
        pwdNew = request.form.get("new_password")
        pwdConf = request.form.get("confirmation")

        if not pwdOld:
            return apology("You must provide your actual password", 403)

        # Check.
        elif not pwdNew or not pwdConf:
            return apology("You must enter both, new password and confirmation", 403)

        # Check if new passwords match
        elif pwdNew != pwdConf:
            return apology("Your new password fields doesn't match", 403)

        else:
            pwdhash = db.execute("SELECT hash FROM users WHERE id=:user_id", user_id=user_id)
            i = pwdhash[0]["hash"]
            state = check_password_hash(i, pwdOld)

            if state == False:
                return apology("Your password is incorrect.")
            else:
                newHash = generate_password_hash(pwdNew)
                db.execute("UPDATE users SET hash=:newHash WHERE id=:user_id", newHash=newHash, user_id=user_id)
                return redirect("/")
    else:
        return render_template("changepwd.html")

def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
