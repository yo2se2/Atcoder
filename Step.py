N = int(input())
A = list(map(int,input().split()))
answer = 0
min = A[0]

for i in range(1,N):
    if A[i] < min:
        answer += min - A[i]
    elif min < A[i]:
        min = A[i]

print(answer)
