N = int(input())

ans = float('inf')
for i in range(1,int(N**0.5)+1):
    a = i
    b = N//i
    r = N-(a*b)
    d = abs(a-b)
    score = r+d
    ans = min(ans,score)
print(ans)