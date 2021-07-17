N = int(input())
X = list(map(int, input().split()))
Min = 1 << 20

for i in range(1, 101):
    score = 0
    for j in range(N):
        score += (X[j] - i)**2
    if score < Min:
        Min = score
print(Min)