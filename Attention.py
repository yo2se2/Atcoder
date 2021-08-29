from collections import Counter

N = int(input())
S = list(input())

l = {'W' : 0, 'E' : 0}
r = Counter(S)
Min = 3*(10**5) + 10
for i in range(N):
    ans = 0
    r[S[i]] -= 1
    ans = l['W'] + r['E']
    l[S[i]] += 1

    if ans < Min:
        Min = ans
print(Min)




