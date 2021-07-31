N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
B.sort()

Min = 10**9+1
def binary_search(x):
    low = 0
    high = M-1

    while low <= high:
        mid = (low + high)//2
        if B[mid] == x:
            return 0
        elif B[mid] > x:
            high = mid - 1
        elif B[mid] < x:
            low = mid + 1
    if low >= M:
        low = M-1
    if high <= 0:
        high = 0
    ans = min(abs(x-B[low]),abs(x-B[high]))
    return ans

for a in A:
    ans = binary_search(a)

    if Min > ans:
        Min = ans
print(Min)