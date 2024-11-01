# с клавиатуры вводится число N, а затем – N натуральных чисел.
# Определить минимальное и максимальное среди простых чисел
# (которые делятся на сами не себя и на 1).
# Если таких чисел не было, вывести "нет".

from math import sqrt

N = int(input())

P =[]
n = 0
for j in range(N):
    s = int(input())
    i = 0
    if s != 1:
        for i in range(2, int(sqrt(s))+1):
            if s % i == 0:
                n += 1
                break
        else:
            P.append(s)

if len(P) == 0:
    print('sdjgnsg')
else:
    print(max(P), min(P))

"6\n1\n4\n5\n10\n13\n17\n"

