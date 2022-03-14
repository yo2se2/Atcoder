N = int(input())
A = list(map(int, input().split()))
c = 0
d = 0
e = 0
for i in range(N):
    if A[i] % 4 == 0:
        c += 1
    elif A[i] % 2 == 0:
        e += 1
    else:
        d += 1


if c+1 >= d + (e%2):
    print('Yes')
else:
    print('No')