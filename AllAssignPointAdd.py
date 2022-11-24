N = int(input())
A = list(map(int, input().split()))
Q = int(input())

all = None
d = {}

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        all = q[1]
        d = {}
    elif q[0] == 2:
        if all:
            d[q[1]] =  q[2] + d.get(q[1],0)
        else:
            d[q[1]] = d.get(q[1],0) + q[2]
    elif q[0] == 3:
        if all:
            print(all + d.get(q[1],0))
        else:
            print(A[q[1]-1]+d.get(q[1],0))

