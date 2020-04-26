# Задание 2


my_list = [20, 1, 5, 2, 3 ,1 , 0, 5, 6, 100, 2, 6, 5, 4, 2, 1000]
new_list = []
i = 1
for el in my_list[1:]:
    if my_list[i] > my_list[i-1]:
        new_list.append(el)
        i = i + 1
    else:
        i = i + 1
print(f"Исходный список: {my_list}")
print(f"Новый список: {new_list}")