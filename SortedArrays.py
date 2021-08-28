N = int(input())
A = list(map(int, input().split()))
cnt = 1
i = 0
while i < N-1:
    if A[i+1] == A[i]:
        i += 1
        continue
    elif A[i+1] > A[i]:
        while i < N-1 and A[i+1] >= A[i]:
            i = i + 1
            if i == N-1:
                break
        if i < N-1:
            cnt += 1
            i = i + 1
    elif A[i+1] < A[i]:
        while A[i+1] <= A[i]:
            i = i + 1
            if i == N-1:
                break
        if i < N-1:
            cnt += 1
            i = i + 1

print(cnt)




