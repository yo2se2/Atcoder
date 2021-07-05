from math import factorial
m = []
P = int(input())
cnt = 0
for i in range(1,11):
    m.append(factorial(i))
m.append(10 ** 8)

def binary_search(x: int):
    low = 0
    high = 10
    while high >= low:
        mid = (high+low)//2
        if m[mid] == x:
            return mid
        if m[mid] < x:
            low = mid + 1
        elif m[mid] > high:
            high = mid - 1
    return high

while P > 0:

    idx = binary_search(P)
    c = (P // m[idx])
    cnt += c
    a = c*m[idx]
    # print("P({})-a({})={} コインの枚数{}: 合計{}".format(P,c*m[idx], P-(c*m[idx]),c,cnt))
    P -= c * m[idx]

print(cnt)