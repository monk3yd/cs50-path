# Import Flask's Functions
from flask import Flask, redirect, render_template, request

# Define Flask App
app = Flask(__name__)

todos = []

# Creates Default Route
@app.route("/")
def tasks():
    return render_template("tasks.html", todos=todos)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    else:
        todo = request.form.get("task")
        todos.append(todo)
        return redirect("/")
