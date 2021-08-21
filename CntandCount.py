from collections import Counter

N = int(input())
S = list(input())

c = Counter(S)
ans = 0
Max = 0

s = set()
for i in range(N):

    c[S[i]] -= 1

    if not(S[i] in s):
        s.add(S[i])
        if c[S[i]] > 0:
            ans += 1
    else:
        if c[S[i]] == 0:
            ans -= 1

    if Max < ans:
        Max = ans
print(Max)
