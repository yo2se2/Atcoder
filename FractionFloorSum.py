#格子数

N = int(input())
n = N
d = 1
ans = 0

while d <= N**0.5:
    ans += N//d
    d += 1

ans *= 2
ans -= (int(N**0.5))**2
print(ans)