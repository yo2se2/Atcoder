A, B, C = map(int, input().split())

l = [A, B, C]
l.sort()
ans = 0

ans += l[2] - l[1]

l[0] += l[2] - l[1]
if (l[2]-l[0])%2 == 0:
    ans += (l[2]-l[0])//2
else:
    ans += (l[2]-l[0])//2 + 2

print(ans)




