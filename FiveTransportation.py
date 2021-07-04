from math import ceil

N = int(input())
P = []

cnt = 0
for _ in range(5):

    p = int(input())
    P.append(p)
b = min(P)
i = P.index(b)
# ボトルネックを全員が超えてからの時間
a = 5-1-i
t = a
# ボトルネックでの処理時間（N人をさばくのにかかる時間）+ ボトルネックに人が到着する時間
t += i + ceil(N/b)
print(t)