import heapq

Q = int(input())
q = []
#空のリストq　を優先度つきキューへ変換
heapq.heapify(q)
offset = 0

for _ in range(Q):
    query = input()
    Q = list(query.split(' '))
    P = int(Q[0])

    if P == 1:
        X = int(Q[1])
        heapq.heappush(q, X-offset)

    if P == 2:
        X = int(Q[1])
        offset += X

    if P == 3:
        print(heapq.heappop(q)+offset)


