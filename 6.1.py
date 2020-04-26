from itertools import count

from sys import argv
# Задание 6.1

def my_count(start, stop):
    for el in count(start):
        if el > stop:
            break
        else:
            print(el)

tru_count, sta, sto = argv

print("Начальное число", sta)
print("Конечное число", sto)
my_count(sta, sto)

