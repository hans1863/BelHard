# Simple calculator


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


number_1 = float(input("Введите первое число: "))
oprtr = input("Введите операцию: ")
number_2 = float(input("Введите второе число: "))

if oprtr == "+":
    print(number_1, "+", number_2, "=", add(number_1, number_2))

elif oprtr == "-":
    print(number_1, "-", number_2, "=", subtract(number_1, number_2))

elif oprtr == "*":
    print(number_1, "*", number_2, "=", multiply(number_1, number_2))

elif oprtr == "/":
    print(number_1, "/", number_2, "=", divide(number_1, number_2))
else:
    print("Invalid input")
