import numpy as np

N = int(input())
A = list(map(int, input().split()))
mod = 998244353
ans = np.zeros(10, np.int64)

ans[A[0]] = 1

for i in range(1, N):
    B = np.zeros(10, np.int64)
    # print("Bは{}".format(B))
    for j in range(10):
        B[(j + A[i]) % 10] += ans[j]
        B[(j * A[i]) % 10] += ans[j]
    ans = B % mod
for a in ans:
    print(a)


