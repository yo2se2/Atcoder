N = int(input())
S = {}
Max = 0
for _ in range(N):
    s = input()
    if s in S:
        S[s] += 1
    else:
        S[s] = 1
    if Max < S[s]:
        Max = S[s]
        idx = s


print(idx)