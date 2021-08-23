N = int(input())

A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
csum1 = [A1[0]]
csum2 = [A2[0]]

for i in range(1,N):
    csum1.append(csum1[i-1] + A1[i])
    csum2.append(csum2[i-1] + A2[i])

Max = 0
for i in range(N):
    ans = 0
    ans += csum1[i] + A2[i] + (csum2[-1] - csum2[i])
    if Max < ans:
        Max = ans

print(Max)