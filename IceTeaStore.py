Q, H, S, D = map(int, input().split())
N = int(input())
ans = 0
q2 = 8*Q
h2 = 4*H
s2 = 2*S
d2 = D
a = min(q2,h2,s2,d2)

q1 = 4*Q
h1 = 2*H
s1 = S
b = min(q1,h1,s1)
if N > 1:
    ans += a * (N//2)
    N -= 2*(N//2)

if N > 0:
    ans += b
    N -= 1

print(ans)