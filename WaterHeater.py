N, W = map(int,input().split())

imos = [0] * 10**6
#イモス法による累積和
for _ in range(N):
    s, t, p = map(int,input().split())
    imos[s] += p
    imos[t] -= p

for i in range(1,len(imos)):
    imos[i] += imos[i-1]

max_value = max(imos)
if max_value > W:
    print('No')
else:
    print('Yes')
