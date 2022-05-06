# Not so simple calculator


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    try:
        return num1 / num2
    except Exception:
        print("Can't divide by zero")


counter = 0

while True:

    number_1 = input("Введите первое число: ")

    if number_1 == "стоп":
        break

    try:
        number_1 = float(number_1)
    except Exception:
        print("Enter valid number")
        continue

    oprtr = input("Введите операцию: ")

    if oprtr not in ["+", "-", "*", "/"]:
        print("Operator is invalid")
        continue
    else:
        pass

    try:
        number_2 = float(input("Введите второе число: "))
    except Exception:
        print("Enter valid number")
        continue

    if oprtr == "+":
        print(number_1, "+", number_2, "=", add(number_1, number_2))
        # counter += counter

    elif oprtr == "-":
        print(number_1, "-", number_2, "=", subtract(number_1, number_2))
        # counter += counter

    elif oprtr == "*":
        print(number_1, "*", number_2, "=", multiply(number_1, number_2))
        # counter += counter

    elif oprtr == "/":
        print(number_1, "/", number_2, "=", divide(number_1, number_2))
        # counter += counter

    else:
        print("Invalid input")
counter += 1

print(f"{counter} operations were executed")
