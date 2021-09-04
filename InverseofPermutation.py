N = int(input())
p = list(map(int, input().split()))
q = [0 for _ in range(N)]

for i in range(N):
    q[p[i]-1] = i+1

ans = ' '.join(map(str,q))
print(ans)
