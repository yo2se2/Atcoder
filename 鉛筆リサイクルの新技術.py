m, n, N = map(int, input().split())
ans = 0
num = N
c = 0
while num > 0:
    ans += num
    c += num % m
    num = (num//m) * n


    if c >= m:
        num += n
        c -= m
print(ans)
