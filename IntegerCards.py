import heapq

N, M = map(int, input().split())
A = list(map(int, input().split()))
t = sum(A)

a = heapq.heapify(A)

conv = []
for _ in range(M):
    b, c = map(int, input().split())
    conv.append((b,c))

conv.sort(key=lambda x:x[1])
f = True
while conv:
    if f:
        i,v = conv.pop()
        for j in range(i):
            m = heapq.heappop(A)
            if m < v:
                heapq.heappush(A,v)
                t += v-m
            else:
                f = False
    else:
        break
print(t)





