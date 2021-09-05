S = list(input())
l = len(S)

ans = 0

for i in range(len(S)):
    if S[i] == 'U':
        ans += l-(i+1)
        ans += 2*(i)
    elif S[i] == 'D':
        ans += 2*(l-(i+1))
        ans += i
print(ans)


