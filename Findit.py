N = int(input())
A = list(map(int, input().split()))
A = [0] + A
vis = [False for _ in range(N+1)]

def DFS(s):
    stack = [s]
    x = s
    while stack:
        x = stack.pop()
        vis[x] = True

        nxt = A[x]
        if not(vis[nxt]):
            stack.append(nxt)
        else:
            return nxt


def loop(s):
    log = [s]
    x = s
    nxt = A[s]
    while nxt != s:
        log.append(nxt)
        a = nxt
        nxt = A[nxt]
        x = a
    return log

ans = loop(DFS(1))

print(len(ans))
print(' '.join(map(str,ans)))