N = int(input())
a = list(map(int, input().split()))
A = []
for i in range(N):
    A.append((a[i],i+1))

A.sort(key = lambda x:x[0], reverse=True)

for ans in A:
    print(ans[1])

