from collections import defaultdict

N = int(input())

imos = defaultdict(int) #辞書型の初期値を0としてくれる。
ans = [0 for _ in range(N+1)]

for _ in range(N):
    a, b = map(int, input().split())
    imos[a] += 1
    imos[a+b] -= 1

key = sorted(imos.keys())

num = 1
cnt = 0

for i in key:
    ans[cnt] += i-num
    cnt += imos[i]
    num = i

print(' '.join(map(str,ans[1:])))