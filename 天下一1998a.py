a = [100, 100, 200]

for i in range(3,20):
    ans = a[i-1] + a[i-2] + a[i-3]
    a.append(ans)
print(a[-1])