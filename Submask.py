N = int(input())

ans = [0]
ad = [0]
b = bin(N)[-1:1:-1]

i = 0

for k in b:
    if k == '1':
        l = []
        a = 2**i
        for p in ans:

            L = a + p
            l.append(L)
        ans += l
    i += 1
for a in ans:
    print(a)
