from itertools import permutations

S, K = input().split()

p = set(permutations(S))
P = set(p)
ans = sorted(P)

print(''.join(ans[int(K)-1]))
