#　尺取り法もどき

N, K = map(int, input().split())
P = list(map(int, input().split()))
e = 0
ce = [0]
ans = 0
def calc_exp(x):
    S = x*(2+(x-1))//2
    return S/x

for p in P:
    e += calc_exp(p)
    #期待値の累積和
    ce.append(e)
for i in range(N-K+1):
    a = ce[K+i]-ce[i]
    if ans < a:
        ans = a
print(ans)