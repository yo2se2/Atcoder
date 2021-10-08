S = list(input())

c = S[0]
ans = 0
for i in range(1,len(S)):
    if c == S[i]:
        continue
    else:
        c = S[i]
        ans += 1

print(ans)