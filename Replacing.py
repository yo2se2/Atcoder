# 差分更新

from collections import  Counter

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

S = sum(A)
cnt = Counter(A)

for _ in range(Q):
    b, c = map(int, input().split())
    add = c-b
    S += add*cnt[b]
    cnt[c] += cnt[b]
    cnt[b] = 0
    print(S)