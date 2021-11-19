S = list(input())
N = int(input())
L = [i for i in range(len(S))]

for _ in range(N):
    l, r = map(int, input().split())
    reverse = S[l-1:r]
    reverse = reverse[::-1]
    ans = S[0:l-1] + reverse + S[r:]
    S = ans
print(''.join(ans))
