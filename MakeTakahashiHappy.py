from  collections import deque

H, W  = map(int, input().split())
A = []

for _ in range(H):
    a = list(map(int, input().split()))
    A.append(a)

def BFS(sx, sy):
    x, y = sx, sy
    q = deque([])


