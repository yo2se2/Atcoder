N = int(input())
p = list(map(int, input().split()))
f = [False for _ in range(max(p)+10)]
Min = 0
for P in p:
    i = Min
    f[P] = True
    while f[i]:
        i += 1
    Min = i
    print(i)

