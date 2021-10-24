import heapq

N, M = map(int, input().split())
A = list(map(int, input().split()))
A = list(map(lambda x: x*(-1), A))
#空のリストq　を優先度つきキューへ変換
heapq.heapify(A)

while M > 0:
    a = (heapq.heappop(A)*-1) // 2
    heapq.heappush(A, -a)
    M -= 1

ans = 0
for a in A:
    ans += -a

print(ans)
