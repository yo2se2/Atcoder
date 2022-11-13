from collections import deque
from collections import defaultdict

N = int(input())
n = defaultdict(list)
d = deque()
S = {1}
for _ in range(N):
    a, b = map(int, input().split())
    n[a].append(b)
    n[b].append(a)

def BFS(s: int) -> int:
    d.append(s)
    ans = 0

    while d:
        x = d.popleft()
        ans = max(ans, x)

        for nx in n[x]:
            if not(nx in S):
                d.append(nx)
                S.add(nx)
    return ans


print(BFS(1))