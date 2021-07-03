
N = int(input())
X = list(map(int, input().split()))
sortX = sorted(X)
m = ((N // 2) - 1)

def binary_search(x):
    low = 0
    high = N-1

    while high > low:
        mid = (high + low) // 2
        if sortX[mid] < x:
            low = mid + 1
        else:
            high = mid
    return (high+low)//2

for i in range(N):
    a = binary_search(X[i])
    if a < (N/2):
        print(sortX[N//2])
    elif  a >= N / 2:
        print(sortX[(N//2)-1])
