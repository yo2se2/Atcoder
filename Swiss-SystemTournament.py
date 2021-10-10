N, M = map(int, input().split())
A = []
s = [[0,i] for i in range(2*N)]

for _ in range(2*N):
    a = list(input())
    A.append(a)

w1 = [('G','C'),('P','G'),('C','P')]
w2 = [('G','P'),('P','C'),('C','G')]

for m in range(M):
    for i in range(N):
        h = (A[s[2*i][1]][m],A[s[2*i+1][1]][m])

        if h in w1:
            s[2*i][0] -= 1
        elif h in w2:
            s[2*i+1][0] -= 1

    s.sort()


for ans in s:
    print(ans[1]+1)