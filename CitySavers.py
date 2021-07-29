N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
cnt = 0

for i in range(N):
    if A[i] > B[i]:
        cnt += B[i]
    else:
        if A[i+1] + A[i] >= B[i]:
            cnt += B[i]
        else:
            cnt += A[i] + A[i+1]
        A[i+1] = max(A[i+1]-(B[i]-A[i]),0)


print(cnt)