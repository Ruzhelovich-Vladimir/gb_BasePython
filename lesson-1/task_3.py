"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

USR_N = input("Enter n number: ")

N_VALUE = int(USR_N)
NN_VALUE = int(USR_N * 2)
NNN_VALUE = int(USR_N * 3)

print(
    f"Task result: {N_VALUE} + {NN_VALUE} + {NNN_VALUE} = {N_VALUE + NN_VALUE + NNN_VALUE}")
