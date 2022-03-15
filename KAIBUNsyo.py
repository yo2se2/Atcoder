N = int(input())
A = list(map(int, input().split()))

ans = 0
# Union-Find木
# 1. makeTree(x) : 新しくxを根とした木を作る
# 2. findRoot(x) : xを含む木の根を求める。
# 3. union(x,y) : 指定された2つの要素x,yを含む木を併合する。
# 4. isSame(x,y) : x,yが同じ木にあるのかを根が同じかで判定

class UnionFind():
    def __init__(self,n):
        self.n = n
        self.parents = [i for i in range(self.n+1)]
        self.ans = 0

    def findRoot(self,x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.findRoot(self.parents[x])
            return self.parents[x]

    def union(self,x,y):
        x = self.findRoot(x)
        y = self.findRoot(y)
        if x == y:
            return 0
        self.parents[x] = y
        self.ans += 1

    def isSame(self,x,y):
        return self.findRoot(x) == self.findRoot(y)

p  = UnionFind(2*(10**5)+10)


for i in range(N//2):
    p.union(A[-(i+1)], A[i])

print(p.ans)