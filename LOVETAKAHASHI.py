N = int(input())
W = list(input().split())

cnt = 0

W[N-1] = W[N-1][:-1]

for i in range(N):

    if W[i] == 'Takahashikun' or W[i] == 'TAKAHASHIKUN' or W[i] == 'takahashikun':
        cnt += 1

print(cnt)