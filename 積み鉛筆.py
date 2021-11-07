N = int(input())
K = list(map(int, input().split()))
L = [0 for _ in range(N)]
L[0], L[N-1] = K[0], K[-1]
K.append(K[-1])

for i in range(N-1):
    if K[i] < K[i+1]:
        L[i+1] = K[i]
    elif K[i] >= K[i+1]:
        L[i+1] = K[i+1]
L = map(str, L)
print(' '.join(L))
