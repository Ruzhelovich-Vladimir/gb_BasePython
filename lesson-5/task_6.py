"""
6)	Необходимо создать (не программно) текстовый файл, где каждая строка
    описывает учебный предмет и наличие лекционных, практических и
    лабораторных занятий по этому предмету и их количество. Важно, чтобы
    для каждого предмета не обязательно были все типы занятий. Сформировать
    словарь, содержащий название предмета и общее количество занятий по нему.
    Вывести словарь на экран.
        Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                  Физика:   30(л)   —   10(лаб)
                             Физкультура:   —   30(пр)   —
    Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

from re import sub
import json


FILENAME = "text_6.txt"
JSON_FILENAME = "text_6.json"
RESULT = {}

try:
    with open(file=FILENAME, mode="r", encoding="utf-8") as f:
        while True:
            STR = f.readline()
            if len(STR) == 0:
                break
            LST = STR.split(":")
            SUBJECT = LST[0]
            # Удаляю все символы кроме букв и пробелов
            STR_TEMP = sub(r"[^[\d\s]", "", LST[1][:-1])
            # Удаляю лишние проблелы
            STR_TEMP = sub(r"\s+", " ", STR_TEMP)
            # Удаляю лишние проблелы начале строки
            STR_TEMP = sub(r"^\s+", "", STR_TEMP)
            # Удаляю лишние проблелы в конце строки
            STR_TEMP = sub(r"\s+$", "", STR_TEMP)
            HOURS_LST = [float(ELEM) for ELEM in STR_TEMP.split(" ")]
            HOURS = sum(HOURS_LST)
            # Если ключ существует, то значение сохраняем в переменную VAL
            VAL = RESULT.get(f"{SUBJECT}", 0)
            RESULT.update({SUBJECT: HOURS + VAL})
    with open(JSON_FILENAME, mode="w", encoding="utf-8") as f:
        json.dump(RESULT, f, sort_keys=True, indent=2)
except IOError:
    print("Ошибка достапа к файлу")
except ValueError:
    print("Строка не является числом")
else:
    print(f"Ок.")
