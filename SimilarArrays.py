N = int(input())
A = list(map(int, input().split()))

odd = 1
comb = 3**N
for a in A:
    if a % 2 == 0:
        odd *= 2

print(comb-odd)

