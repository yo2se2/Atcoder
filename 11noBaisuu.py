N = list(input())
N = N[::-1]
Even = 0
Odd = 0

for idx, n in enumerate(N):
    if (idx+1) % 2 != 0:
        Odd += int(n)
    else:
        Even += int(n)

print(Even, Odd)
