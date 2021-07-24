# 尺取り法

N = int(input())
a = list(map(int, input().split()))
l,  r, ans = 0, 0, 0

while l < N:
    s = l
    ans += 1
    r += 1

    while r < N and a[l] < a[r]:
        ans += r - s + 1
        l += 1
        r += 1
    l = r

print(ans)