"""
3)	Создать текстовый файл (не программно), построчно записать
    фамилии сотрудников и величину их окладов (не менее 10 строк).
    Определить, кто из сотрудников имеет оклад менее 20 тыс.,
    вывести фамилии этих сотрудников. Выполнить подсчет средней
    величины дохода сотрудников.
        Пример файла:
            Иванов 23543.12
            Петров 13749.32
"""

FILENAME = "task_3.txt"
FILENAME = "text_3.txt"
SEPARATOR = " "
SHOW_SALARY = 20000

SUM = 0
INX = 0
try:
    with open(file=FILENAME, mode="r", encoding="utf-8") as f:
        while True:
            STR = f.readline()[:-1]
            if len(STR) == 0:
                break
            LST = STR.split(SEPARATOR)
            SURNAME, SALARY = LST[0], float(LST[1])
            if SALARY < SHOW_SALARY:
                print(SURNAME, SALARY)
            SUM += SALARY
            INX += 1

except IOError:
    print("Ошибка достапа к файлу")
except ValueError:
    print(f"Ошибка преобразования {LST[1][:-1]}")
else:
    print(f"Средний общий доход: {SUM/INX:.2f}")
