N = int(input())
A = list(map(int, input().split()))

rank = [0] * N
c = 1
for i in range(N):
    rank[A[i]-1] = c
    c += 1

rank_str = [str(a) for a in rank]
rank_str = " ".join(rank_str)
print(rank_str)