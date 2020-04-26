from sys import argv

from itertools import cycle
# Задание 6.2


def my_cycle(start, stop):
    for el in cycle(start):
        if el > stop:
            break
        else:
            print(el)


tru_cycle, sta, sto = argv
print("Начальное число", sta)
print("Конечное число", sto)

my_cycle(sta, sto)