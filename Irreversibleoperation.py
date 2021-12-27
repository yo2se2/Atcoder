S = input()
c = 0
ans = 0

for s in S:
    if s == 'B':
        c += 1
    if s == 'W':
        ans += c
print(ans)