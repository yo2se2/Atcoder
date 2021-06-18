X = int(input())

#エラトステネスの篩
def get_prime(x):
    is_prime = [True for _ in range(x+1)]
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2,int(x**0.5)+1):
        if is_prime[i] == False:
            continue
        else:
            for j in range(i**2,x+1,i):
                is_prime[j] = False
    return  [i for i in range(x+1) if is_prime[i]]



primes = get_prime(10**6)
#素数リストで二分探索を行う
low = 0
high = len(primes)-1


while high > low:
    mid = (low + high) // 2
    if primes[mid] < X:
        low = mid + 1
    else:
        high = mid
print(primes[low])