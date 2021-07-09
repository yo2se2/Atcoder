A, B, N = map(int, input().split())

x = B-1
if N > x:
    ans = ((A*x)//B) - (A*(x//B))
else:
    ans = ((A*N)//B) - (A*(N//B))
print(ans)