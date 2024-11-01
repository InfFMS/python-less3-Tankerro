# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, сколько было введено простых натуральных чисел
# (которые делятся только сами на себя и на 1), и сколько сост
from math import sqrt

s = int(input())
p = 0
n = 0
while s != 0:
    if s != 1:
        for i in range(2, int(sqrt(s))+1):
            if s % i == 0:
                n += 1
                break
        else:
            p+=1
    s = int(input())


print(f"Простых чисел: {p} и Составных чисел: {n}")