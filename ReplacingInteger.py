N, K = map(int, input().split())
Min = N

if N % K == 0:
    print(0)
else:
    a = N // K
    b = (N // K) + 1
    ans = min(abs(N-(a*K)),abs(N-(b*K)))
    print(ans)