K, A, B = map(int, input().split())

if B - A <= 2:
    ans = K + 1
else:
    ans = A
    K -= A-1
    if K > 0:
        ans += (K // 2)*(B-A) + (K % 2)
    else:
        ans = K + 1


print(ans)

