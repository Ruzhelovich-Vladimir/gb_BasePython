"""
2. Пользователь вводит время в секундах. Переведите время в часы, минуты и
секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""

USR_SEC = int(input("Enter the number of seconds: "))

HOUR = int(USR_SEC // 3600)
SEC = int(USR_SEC % 60)
MIN = int(((USR_SEC - SEC) % 3600)/60)

print(f"The reformat time result: {HOUR:0>2d}:{MIN:0>2d}:{SEC:0>2d}")
