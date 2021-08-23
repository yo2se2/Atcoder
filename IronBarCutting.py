#　累積和?

N = int(input())
A = list(map(int, input().split()))
Min = 10 ** 13
c = 0
csum = []
for a in A:
    c += a
    csum.append(c)

t = csum[-1]
for l in csum:
    r = t - l

    ans = abs(l - r)

    if ans < Min:
        Min = ans
print(Min)

