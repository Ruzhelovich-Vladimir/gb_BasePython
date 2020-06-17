"""
3)	Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к
	какому времени года относится месяц (зима, весна, лето, осень).
	Напишите решения через list и через dict.
"""
MONTH_LIST = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль",
              "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]

MONTH_DICT = {1: "январь",
              2: "февраль",
              3: "март",
              4: "апрель",
              5: "май",
              6: "июнь",
              7: "июль",
              8: "август",
              9: "сентябрь",
              10: "октябрь",
              11: "ноябрь",
              12: "декабрь"
              }

USR_MONTH = int(input("Введите порядковый номер месяца:"))

print(f"Результат через список  -{MONTH_LIST[USR_MONTH-1]}")
print(f"Результат через словарь -{MONTH_DICT[USR_MONTH]}")
