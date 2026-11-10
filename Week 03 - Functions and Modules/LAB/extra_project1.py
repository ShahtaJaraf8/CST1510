
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


n1 = float(input("What's the first number?: "))

keep_going = True


while keep_going:
    
    operator = input("Pick an operation (+, -, *, /): ")
    n2 = float(input("What's the next number?: "))
    
    if operator == "+":
        result = add(n1, n2)
    elif operator == "-":
        result = subtract(n1, n2)
    elif operator == "*":
        result = multiply(n1, n2)
    elif operator == "/":
        result = divide(n1, n2)
    else:
        result = "Invalid operator"

    print(f"{n1} {operator} {n2} = {result}")

    choice = input(f"Type 'y' to continue with the result, or 'n' to start over: ")

    if choice == "y":
        n1 = result  # 13. If they type "y", set n1 = result
    else:
        n1 = float(input("What's the first number?: "))  # 14. Otherwise, ask for a new first number and store it in n1