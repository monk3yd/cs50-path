def main():
    expression = input("Expression: ")
    operators = expression.split(" ")

    x = operators[0]
    y = operators[1]
    z = operators[2]

    # pass in operator
    answer = calculate(x, y, z)
    print(answer)


def calculate(x, operator, z):
    if operator == "+":
        expr_result = add(x, z)
    elif operator == "-":
        expr_result = substract(x, z)
    elif operator == "*":
        expr_result = multiply(x, z)
    else:
        expr_result = divide(x, z)

    return str(expr_result)


def add(n1, n2):
    return float(n1) + float(n2)


def substract(n1, n2):
    return float(n1) - float(n2)


def multiply(n1, n2):
    return float(n1) * float(n2)


def divide(n1, n2):
    return float(n1) / float(n2)


if __name__ == "__main__":
    main()
