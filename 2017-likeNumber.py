#エラトステネスの篩 + α
def primes(x):
    #素数判定のための真偽値
    is_prime = [True] * (x+1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2,int(x**0.5)+1):
        #False(素数でないもの)はスルー
        if not is_prime[i]:
            continue
        #素数を発見すると素数の倍数であるものをFalseに置き換える。
        for j in range(i **  2, x + 1,i):
            is_prime[j] = False
    #2017に似た数を探す
    likeNum = [0] * (x+1)
    for i in range(3,x + 1):
        if is_prime[i] and is_prime[int((i+1)/2)] == True:
            likeNum[i] = 1

    #累積和によって素数の個数を求めるため，素数を1,素数以外を０で置き換える
    return  likeNum

#実装

x = 10**5
prime_list = primes(x)




c = [0]
for i in range(1,x):
    c.append(prime_list[i] + c[i-1])
Q = int(input())
for _ in range(Q):
    l, r = map(int,input().split())
    print(c[r]-c[l-1])