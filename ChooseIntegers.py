A, B, C = map(int, input().split())
i = 1

ans = 'NO'
while i < B:
    if (A * i) % B != C:
        i += 1
        continue
    else:
        ans = 'YES'
        break
print(ans)
