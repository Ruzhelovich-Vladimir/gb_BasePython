"""
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

USR_INT = int(input("Enter 	integer number: "))

MAX_RESULT = 0

while True:
    MAX_RESULT = max(USR_INT % 10, MAX_RESULT)
    USR_INT //= 10
    if USR_INT == 0 or MAX_RESULT == 9:
        break

print(f"Result task: {MAX_RESULT}")
