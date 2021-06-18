N = int(input())
answer = -1
min = 100000
L = list(str(N))
n = len(L)
flag = False
#bit全探索
for i in range((2**n)-1):
    bit = []
    Dnum = 0
    for j in range(n):
        if (i >> j) & 1:
            bit.append(1)
            Dnum += 1
        else:
            bit.append(0)

    a = [L[idx] for idx in range(n) if bit[idx] == 0]
    check  = int("".join(map(str, a)))

    if (check % 3) == 0 and (min > Dnum):
        min = Dnum

if (min == 100000):
    min = -1

print(min)