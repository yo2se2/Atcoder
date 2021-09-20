N = int(input())
c = [0 for _ in range(10**5+10)]
A = list(map(int, input().split()))

for a in A:
    c[a] += 1
    c[a-1] += 1
    c[a+1] += 1

print(max(c))