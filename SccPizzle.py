N, M = map(int, input().split())

if M < (2 * N):
    ans = M // 2
else:
    ans = N + ((M - 2*N) // 4)

print(ans)