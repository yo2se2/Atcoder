from itertools import combinations

N = int(input())
X = []
Y = []
ans = 0
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

def calc_dist(i,j):
    return ((X[i]-X[j])**2 + (Y[i]-Y[j])**2)**0.5

comb = list(combinations(list(range(N)),2))

for i, j in comb:
    dis = calc_dist(i,j)
    if ans < dis:
        ans = dis
print(ans)