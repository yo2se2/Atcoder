N = int(input())
p = list(map(int, input().split()))
cnt = 0

for i in range(N-1):
    if i+1 == p[i]:
        p[i] , p[i+1] = p[i+1], p[i]
        cnt += 1

if p[-1] == N:
    cnt += 1

print(cnt)