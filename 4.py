# Задание 4

spisok = [0, 0, 1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9]
new_spisok = []
i = 0
print(spisok)
for el in spisok:
   schet = spisok.count(el)
   if schet > 1:
       new_spisok.append(el)
       spisok.remove(el)

print(spisok)
print(new_spisok)
