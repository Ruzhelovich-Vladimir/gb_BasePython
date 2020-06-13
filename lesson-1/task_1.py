"""
1. Поработайте с переменными, создайте несколько, выведите на экран, запросите
у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
"""

print("Hi! What's your name?")
NAME = input("Enter your name: ")

USR_COM = input(f"{NAME}! Enter operation any of (+,-,*,/): ")

if USR_COM not in "+-*/" and len(USR_COM) != 1:
    raise ValueError("The operation isn`t defined")

USR_FLOAT_1, USR_FLOAT_2 = input(
    "Please, enter float value: "), input("Yet, enter float value: ")

if USR_COM == "+":
    RESULT = float(USR_FLOAT_1) + float(USR_FLOAT_2)
elif USR_COM == "-":
    RESULT = float(USR_FLOAT_1) - float(USR_FLOAT_2)
elif USR_COM == "*":
    RESULT = float(USR_FLOAT_1) * float(USR_FLOAT_2)
else:
    RESULT = float(USR_FLOAT_1) / float(USR_FLOAT_2)

print(f"Result = {RESULT:9.3f}")
