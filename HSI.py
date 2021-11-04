N, M = map(int, input().split())

t = 1900 * M + 100*(N-M)

x = 2**M

ans = t*x

print(ans)