import numpy as np

H, W = map(int, input().split())

A = []

for _ in range(H):
    a = list(input().split())
    A.append(a)
B = np.array(A).T

for i in range(W):
    print(' '.join(B[i]))