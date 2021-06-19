n = int(input())

data = [0] * (10**6 + 10)
#イモス法による累積和を求める

for _ in range(n):
    a,b = map(int,input().split())
    data[a] += 1
    data[b+1] -= 1



sum = 0
#累積和
for i in range(1,10**6 + 10):
    data[i] += data[i-1]

print(max(data))
