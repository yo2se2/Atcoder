#　優先度つきキュー
import heapq

N, K = map(int, input().split())
P = list(map(int, input().split()))
que = P[:K]

#リストを優先度つきキューへ
heapq.heapify(que)

#最小値の取り出し
print(min(que))

for k in range(K,N):

    minima = heapq.heappop(que)
    minima = max(minima,P[k])
    heapq.heappush(que,minima)
    ans = heapq.heappop(que)
    print(ans)
    heapq.heappush(que,ans)


