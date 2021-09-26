from math import ceil

N = int(input())
A = list(map(int, input().split()))

Min = 10 ** 9


for y in range(-100,101):
    ans = 0
    for x in A:
        ans += (x-y)**2
    if ans < Min:
        Min = ans

print(Min)