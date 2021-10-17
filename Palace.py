N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))
Min = 10 << 10


for i in range(len(H)):
    temp = T - H[i] * 0.006
    if abs(temp-A) < Min:
        Min = abs(temp-A)
        ans = i + 1

print(ans)
