N = int(input())
ans = {}

for _ in range(N):
    s = ''.join(sorted(input()))
    if s in ans:
        ans[s] += 1
    else:
        ans[s] = 1
c = 0
for cnt in ans.values():
    c += cnt*(cnt-1)//2

print(c)