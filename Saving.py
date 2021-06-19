N = int(input())

money = list(range(10**6))
sum = [0] * 10**6
for i in range(1,10**6):
    sum[i] += sum[i-1] + money[i]


#二分探索
high = len(sum)
low = 0

while high > low:
    mid = (high + low) // 2

    if sum[mid] > N:
        high = mid
    elif sum[mid] < N:
        low = mid + 1
    else:
        break

answer =    (high + low) // 2
print(answer)