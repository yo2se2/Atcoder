L, R = map(int, input().split())
S = input()
l = len(S)
if R < l:
    r1 = S[L-1:R]
    r1 = r1[::-1]
    r2 = S[R:]
else:
    r1 = S[L-1:R]
    r1 = r1[::-1]
    r2 = S[R:]

ans = S[:L-1] +  r1 + r2
print(ans)