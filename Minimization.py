

N, K = map(int, input().split())
A = list(map(int, input().split()))

#切り上げの計算
ans = (N-1+K-2)//(K-1)
print(ans)