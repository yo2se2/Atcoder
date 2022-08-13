N, M = map(int, input().split())

class UnionFind():

    #初期は自分自身を親とする。（-1）
    def __init__(self,n):
        self.n = n
        self.parents =[-1] * (n+1)
        self.F = True
    def same(self,x,y):
        return self.find(x) == self.find(y)
    #自分の親を見つける関数
    def find(self,x):
        #parents[x]が負の値であるとき，xは親であるので
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    #
    def union(self,x,y):
        #xの親を検索
        x = self.find(x)
        #yの親を検索
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x,y = y,x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

uf = UnionFind(N)
d = {}
for _ in range(M):
    a, b = map(int, input().split())

    if a in d:
        d[a].add(b)
    else:
        d[a] = set()
        d[a].add(b)
    if b in d:
        d[b].add(a)
    else:
        d[b] = set()
        d[b].add(a)

    if len(d[a]) > 2 or len(d[b]) > 2:
        uf.F = False

    if uf.F and uf.same(a,b): #閉路を作る場合False
        uf.F = False
    else:
        uf.union(a, b)

if uf.F:
    print('Yes')
else:
    print('No')
