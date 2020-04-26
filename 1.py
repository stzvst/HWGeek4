from sys import argv


# Задание 1



script_name, work, price_for_work, prime = argv

work = int(work)
price_for_work =int(price_for_work)
prime = int(prime)

print("Имя скрипта: ", script_name)
print("Проделанная работа: ", work)
print("Рублей в час: ", price_for_work)
print("Премия равна: ", prime)
print("Суммарно вы получите: ", (work * price_for_work) + prime)

