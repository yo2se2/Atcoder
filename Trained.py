N = int(input())
n = []
v = [False for _ in range(N)]
for i in range(N):
    a = int(input())
    n.append(a)

def DFS(s):
    stack = [s]
    c = 0
    while stack:
        x = stack.pop()
        v[x - 1] = True
        nx = n[x-1]
        c += 1
        if not(v[nx-1]):
            if nx == 2:
                return c
            else:
                stack.append(nx)
        else:
            return -1
    return -1

print(DFS(1))




