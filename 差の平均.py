n = int(input())

a = list(map(int,input().split()))
diff_total = 0
for i in range(1,n):
    diff_total += a[i]-a[i-1]
print(diff_total/(n-1))