from itertools import  combinations

N = int(input())
d = list(map(int,input().split()))

L  = list(range(N))

seq = combinations(L,2)
answer = 0

for i in seq:
    answer +=  d[i[0]] * d[i[1]]

print(answer)
