"""
7)	Создать вручную и заполнить несколькими строками текстовый файл,
    в котором каждая строка должна содержать данные о фирме: название,
    форма собственности, выручка, издержки.
        Пример строки файла: firm_1   ООО   10000   5000.
    Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
    а также среднюю прибыль. Если фирма получила убытки, в расчет средней
    прибыли ее не включать.
    Далее реализовать список. Он должен содержать словарь с фирмами и их
    прибылями, а также словарь со средней прибылью. Если фирма получила
    убытки, также добавить ее в словарь (со значением убытков).
    Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
        {“average_profit”: 2000}].
    Итоговый список сохранить в виде json-объекта в соответствующий файл.
    Пример json-объекта:
    [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
    Подсказка: использовать менеджер контекста.
"""

from re import sub
import json

FILENAME = "text_7.txt"
JSON_FILENAME = "text_7.json"
RESULT = [{}, {}]
PROFIT_SUM = 0
PROFIT_INX = 0

try:
    with open(file=FILENAME, mode="r", encoding="utf-8") as f:
        while True:
            STR = f.readline()[:-1]
            if len(STR) == 0:
                break
            # Удаляю лишние проблелы
            STR_TEMP = sub(r"\s+", " ", STR)
            # Удаляю лишние проблелы начале строки
            STR_TEMP = sub(r"^\s+", "", STR_TEMP)
            # Удаляю лишние проблелы в конце строки
            STR_TEMP = sub(r"\s+$", "", STR_TEMP)
            LST = STR_TEMP.split(" ")
            SUBJECT = LST[0]
            PROFIT = float(LST[2]) - float(LST[3])
            if PROFIT >= 0:
                PROFIT_SUM += PROFIT
                PROFIT_INX += 1
            RESULT[0].update({SUBJECT: PROFIT})
    RESULT[1].update({"average_profit": PROFIT_SUM / PROFIT_INX})
    with open(JSON_FILENAME, mode="w", encoding="utf-8") as f:
        json.dump(RESULT, f, indent=4, ensure_ascii=False)
except IOError:
    print("Ошибка достапа к файлу")
except ValueError:
    print("Строка не является числом")
else:
    print(f"Ок.")
