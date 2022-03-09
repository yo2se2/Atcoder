N = int(input())
A = list(map(int, input().split()))

t = sum(A)/N

a = 0

if int(t) == t:
     c = 1
     ans = 0

     for i in range(N):
         a += A[i]
         if a/c == t:
             c = 1
             a = 0
         else:
             ans += 1
             c += 1

else:
    ans = -1

print(ans)