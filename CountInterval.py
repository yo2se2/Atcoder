N, K = map(int, input().split())
A = list(map(int, input().split()))

cs = [0]
c = 0
for i in range(N):
    c += A[i]
    cs.append(c)
m = {}
ans = 0

for i in range(1,N+1):
    if cs[i-1] in m:
        m[cs[i-1]] += 1
    else:
        m[cs[i-1]] = 1
    if cs[i]-K in m:
        ans += m[cs[i]-K]
print(ans)

#二重ループだとTLE → 連想配列を使う

# for l in range(N+1):
#     for r in range(l,N+1):
#         if l == r:
#             continue
#         else:
#             if cs[r]-cs[l] == K:
#                 ans += 1
