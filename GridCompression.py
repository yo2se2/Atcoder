H, W = map(int, input().split())
A = []
At = []
c = ['.' for _ in range(W)]
d = 0
for _ in range(H):
    a = list(input())
    if a != (c):
        A.append(a)
    else:
        d -= 1
c = ['.' for _ in range(H+d)]

for w in range(W):
    at = [b[w] for b in A]
    if at != c:
        At.append(at)

for h in range(H+d):
    print(''.join([b[h] for b in At]))

