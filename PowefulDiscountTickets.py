import heapq

N, M = map(int, input().split())
A = list(map(int, input().split()))
ls = [-1*i for i in A]

heapq.heapify(ls)

for i in range(M):
    pd = (heapq.heappop(ls)*-1)//2


    heapq.heappush(ls,pd*-1)

print(sum(ls)*-1)