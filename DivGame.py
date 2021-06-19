import collections

N = int(input())
ans = 0
def prime_factorize(n):
    a = []

    #偶数→奇数になるまで2で割り続ける
    while n % 2== 0:
        a.append(2)
        n //= 2

    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2

    if n != 1:
        a.append(n)

    return a

c = collections.Counter(prime_factorize(N))


for i in c.values():
    cnt = 1
    while cnt <= i:
        i = i-cnt
        cnt += 1
        ans += 1
print(ans)
