from collections import Counter

N, P = map(int, input().split())

def prime_div(x):
    primes = []
    while x % 2 == 0:
        primes.append(2)
        x //= 2

    i = 3

    while i * i <= x:
        if x % i == 0:
            primes.append(i)
            x //= i
        else:
            i += 2
    if x != 1:
        primes.append(x)
    return primes

p = prime_div(P)
C = Counter(p)
ans = 1

for c in C:
    if C[c] >= N:
        ans *= c**(C[c]//N)

print(ans)






