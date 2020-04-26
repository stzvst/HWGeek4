# Задание 6.2

flag = int(input("Введите число, чей факториал вы хотите увидеть: "))

def fibo_gen():
    i = 1
    for el in range(1,flag+1):
        i = el * i
        yield i

fibo = fibo_gen()
print(fibo)

for el in fibo_gen():
    print(el)