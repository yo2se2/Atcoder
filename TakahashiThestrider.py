from math import ceil

X = int(input())
f = True
k = 1
while f:
    if (k*360) % X == 0:
        f = False
        print((k*360)//X)
    k += 1
