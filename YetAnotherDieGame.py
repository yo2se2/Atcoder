x = int(input())

a = x // 11
b = x % 11
ans = 0
if b > 6:
    ans += 2
elif b == 0:
    ans += 0
else:
    ans += 1
ans += 2*a

print(ans)