N, Q = map(int, input().split())
n = [[] for _ in range(N+1)]
p = [[] for _ in range(N+1)]



for _ in range(Q):
    query = list(map(int,input().split()))

    if query[0] == 1:
        n[query[1]].append(query[2])
        p[query[2]].append(query[1])

    if query[0] == 2:
        n[query[1]].pop()
        p[query[2]].pop()

    if query[0] == 3:
        #先頭車両を探索
        x = int(query[1])

        while True:
            if p[x]:
                x = p[x][0]
            else:
                break
        ans = [x]
        #先頭車両から最終車両まで順番にリストに格納
        while x:
            if n[x]:
                ans.append(n[x][0])
                x = n[x][0]
            else:
                L = len(ans)
                ans = [L] + ans
                ans = list(map(str,ans))
                print(' '.join(ans))
                break
