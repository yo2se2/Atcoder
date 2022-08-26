from collections import defaultdict

N = int(input())
mod = 10**9+7

#素因数分解
def prime_factorization(x):
    primes = defaultdict(int)
    for temp in range(2,x+1):
        # print('--------------')
        # print(temp)
        for d in range(2,int(x**0.5)+1):
            if temp % d == 0:
                cnt = 0
                while temp % d == 0:
                    cnt += 1
                    temp //= d
                primes[d] += cnt
        if temp!= 1:
            primes[temp] += 1
    return primes

pri = prime_factorization(N)
ans = 1
for n in pri.values():
    ans *= (n+1)
print(ans%mod)