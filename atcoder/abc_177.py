# ==========================
# === A - Don't be late
# ==========================
"""
問題文
高橋君は青木君と待ち合わせをしています。
待ち合わせ場所は高橋君の家から D メートル離れた地点であり、待ち合わせの時刻は T 分後です。
高橋君は今から家を出発し、分速 S メートルで待ち合わせ場所までまっすぐ移動します。
待ち合わせに間に合うでしょうか？

制約
1≤D≤10000
1≤T≤10000
1≤S≤10000
入力は全て整数
"""
import sys
input = sys.stdin.readline
D, T, S = map(int, input().split())

dist = S * T
if dist >= D:
  print("Yes")
else:
  print("No")

# ==========================
# === B - Substring
# ==========================
"""
問題文
2 つの文字列 S, T が与えられます。
T が S の部分文字列となるように、S のいくつかの文字を書き換えます。
少なくとも何文字書き換える必要がありますか？
ただし、部分文字列とは連続する部分列のことを指します。例えば、xxx は yxxxy の部分文字列ですが、xxyxx の部分文字列ではありません。

制約
S,T は 1 文字以上 1000 文字以下
T の長さは S の長さ以下
S,T は 英小文字のみを含む
"""
S = input()
T = input()
ans = 999999
for i in range(len(S) - len(T) + 1):
  s = S[i:i + len(T)]
  score = 0
  for i in range(len(s)):
    if s[i] != T[i]:
      score += 1
  ans = min(ans, score)

print(ans)

# ==========================
# === C - Sum of product of pairs
# ==========================
"""
問題文
N 個の整数 A1,...,AN が与えられます。
1≤i<j≤N を満たす全ての組 (i,j) についての Ai×Aj の和を mod(10**9+7) で求めてください。

制約
2≤N≤2×10**5
0≤Ai≤10**9
入力は全て整数
"""
import sys
input = sys.stdin.readline
 
N = int(input())
A = list(map(int, input().split()))
mod = 10 ** 9 + 7

sum_A = sum(A)
ans = 0
for a in A[:-1]:
  sum_A -= a
  ans += a * sum_A

ans %= mod
print(ans)

# ==========================
# === D - Friends
# ==========================
"""
問題文
人 1 から 人 N までの N 人の人がいます。
「人 Ai と人 Bi は友達である」という情報が M 個与えられます。同じ情報が複数回与えられることもあります。
X と Y が友達、かつ、Y と Z が友達ならば、X と Z も友達です。
また、M 個の情報から導くことができない友達関係は存在しません。
悪の高橋君は、この N 人をいくつかのグループに分け、全ての人について「同じグループの中に友達がいない」という状況を作ろうとしています。
最小でいくつのグループに分ければ良いでしょうか？

制約
2≤N≤2×10**5
0≤M≤2×10**5
1≤Ai,Bi≤N
Ai≠Bi
"""
class UnionFind:
  def __init__(self, n):
    self.parent = [-1] * n
    self.rank = [1] * n
    self.count = [1] * n

  def get_root(self, i):
    if self.parent[i] < 0:
      return i
    else:
      self.parent[i] = self.get_root(self.parent[i])
      return self.parent[i]

  def is_same_tree(self, i, j):
    return self.get_root(i) == self.get_root(j)

  def merge(self, i, j):
    i = self.get_root(i)
    j = self.get_root(j)
    if i == j:
      return

    if self.rank[i] > self.rank[j]:
      self.parent[j] = i
      self.rank[i] = max(self.rank[i], self.rank[j] + 1)
      self.count[i] += self.count[j]
    else:
      self.parent[i] = j
      self.rank[j] = max(self.rank[j], self.rank[i] + 1)
      self.count[j] += self.count[i]


n, m = map(int, input().split())
uf = UnionFind(n)
for _ in range(m):
  a, b = [int(i) - 1 for i in input().split()]
  uf.merge(a, b)
print(max(uf.count))

# ==========================
# === E - Coprime
# ==========================
"""
問題文
N 個の整数があります。i 番目の数は Ai です。
「全ての 1≤i<j≤N について、GCD(Ai,Aj)=1」が成り立つとき、{Ai} は pairwise coprime であるといいます。
{Ai} が pairwise coprime ではなく、かつ、GCD(A1,…,AN)=1 であるとき、{Ai} は setwise coprime であるといいます。
{Ai} が pairwise coprime、setwise coprime、そのどちらでもない、のいずれであるか判定してください。
ただし GCD(…) は最大公約数を表します。

制約
2≤N≤10**6
1≤Ai≤10**6
"""
import sys
from math import gcd
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))

g = 0
for a in A:
  g = gcd(g, a)
if g > 1:
  print("not coprime")
  exit()

def factorize(n):
    d = set()
    m = 2
    while m * m <= n:
        while n % m == 0:
            n //= m
            d.add(m)
        m += 1
    if n > 1:
        d.add(n)
    return d

st = set()
for a in A:
    fac = factorize(a)
    if fac.intersection(st):
        print('setwise coprime')
        exit()
    st.update(fac)
print('pairwise coprime')
