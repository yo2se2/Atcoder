#順列全探索
from itertools import permutations

N, K = map(int,input().split())

T = [list(map(int,input().split())) for _ in range(N)]
seq = permutations(range(2,N+1))
answer = 0

for i in seq:
    root = tuple([1]) + i + tuple([1])
    L = len(root)
    loc = 0
    time = 0

    while loc < L-1:
        time += T[root[loc]-1][root[loc+1]-1]
        loc += 1

    if time == K:
        answer += 1

print(answer)