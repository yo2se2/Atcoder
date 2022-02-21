A, B, C, D = map(int, input().split())

def eratones(x):
    is_primes = [True for _ in range(x+1)]
    is_primes[0] = False
    is_primes[1] = False
    c = 2
    while c < x**0.5:
        if is_primes[c]:
            for i in range(c*2,x+1,c):
                is_primes[i] = False
        c += 1
    return [i for i in range(x+1) if is_primes[i]]

primes = eratones(210)

for t in range(A,B+1):
    f = True
    for a in range(C,D+1):
        p = a+t
        if not(p in primes):
            continue
        else:
            f = False
    if f:
        print('Takahashi')
        exit()
print('Aoki')


