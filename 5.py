# Задание 5


my_dict = [el for el in range(100, 1001) if el%2 == 0 ]
print(my_dict[0], my_dict[len(my_dict)-1])
i=1
for el in my_dict:
    i = el * i

print(i)