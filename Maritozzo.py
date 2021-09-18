s1 = input()
s2 = input()
s3 = input()
S = [s1, s2, s3]
T = list(input())

ans = []

for i in T:
    ans.append(S[int(i)-1])

print(''.join(ans))