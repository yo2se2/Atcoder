N = int(input())
P = list(map(int, input().split()))
Min = 3 * (10**5)
ans = 0

for p in P:
    if p < Min:
        ans += 1
        Min = p

print(ans)