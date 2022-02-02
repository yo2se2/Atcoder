R, G, B, N = map(int, input().split())


ans = 0
for r in range(N+1):
    for g in range(N+1):
        b = (N - r*R - g*G)/B
        if b < 0:
            break
        if (N - r*R - g*G)%B == 0:
            ans += 1

print(ans)