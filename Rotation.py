N, Q = map(int, input().split())
S = input()
L  = len(S)
cnt = 0
for _ in range(Q):
    i, x = map(int,input().split())
    if i == 1:
        cnt += x
    elif i == 2:
        print(S[x-((cnt)%L)-1])


