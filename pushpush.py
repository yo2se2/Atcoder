from collections import deque
N = int(input())
A = list(map(int, input().split()))
d = deque([])

for i in range(N):
    if i % 2 == 0:
        d.append(A[i])
    else:
        # insertやpopで要素の先頭を追加削除は時間がかかる。
        d.appendleft(A[i])

if N % 2 != 0:
    print(*list(reversed(d)))
else:
    print(*(d))