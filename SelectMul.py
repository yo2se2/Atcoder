from itertools import permutations

N = list(input())
L = len(N)
Max = 0
for i in range(1,2**(L)-1):
    bit = [0 for _ in range(L)]
    l = []
    r = []
    for j in range(L):
        if (i >> j) & 1 == 1:
            l.append(N[j])
        else:
            r.append(N[j])

    l = list(permutations(l))
    r = list(permutations(r))
    for ll in l:
        ll = int(''.join(ll))
        for rr in r:
            rr = int(''.join(rr))
            ans = ll*rr
            if Max < ans:
                Max = ans


print(Max)




