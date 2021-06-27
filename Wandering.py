N = int(input())
A = list(map(int, input().split()))
x = 0
Max = 0

csum = [0 for _ in range(N)]
potential = [0 for _ in range(N)]

potential[0] = A[0]
csum[0] = A[0]
add = A[0]

for i in range(1,N):
    csum[i] = csum[i-1] + A[i]
    if csum[i] > potential[i-1]:
        potential[i] = csum[i]
    else:
        potential[i] = potential[i-1]
#動作中の最大進路

# print(csum,potential)

for idx, add in enumerate(csum):
    if potential[idx] > 0:
        pMax = x + potential[idx]
        if pMax > Max:
            Max = pMax
    x += add
    if Max < x:
        Max = x

print(Max)