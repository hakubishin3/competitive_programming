# ==========================
# === A - Not
# ==========================
"""
問題文
0 以上 1 以下の整数 x が与えられます。 
x が 0 なら 1 を、1 なら 0 を出力してください。

制約
0≤x≤1
x は整数
"""
x = int(input())
print(int(not x))

# ==========================
# === B - Product Max
# ==========================
"""
問題文
整数 a,b,c,d が与えられます。 
a≤x≤b,c≤y≤d を満たす整数 x,y について、x×y の最大値はいくつですか。

制約
-10**9≤a≤b≤10**9
−10**9≤c≤d≤10**9
入力はすべて整数
"""
a, b, c, d = map(int, input().split())
print(max(a * c, b * d, a * d, b * c))

# ==========================
# === C - Ubiquity
# ==========================
"""
問題文
長さ N の整数の列 A1,A2,…,AN であって以下の条件をすべて満たすものはいくつありますか。
- 0≤Ai≤9
- Ai=0 なる i が存在する。
- Ai=9 なる i が存在する。
ただし、答えはとても大きくなる可能性があるので、10**9+7 で割った余りを出力してください。

制約
1≤N≤10**6
N は整数
"""
N = int(input())
mod = 10**9 + 7
ans = 10 ** N - 9 ** N * 2 + 8 ** N
print(ans % mod)

# ==========================
# === D - Redistribution
# ==========================
"""
問題文
整数 S が与えられます。 すべての項が 3 以上の整数で、その総和が S であるような数列がいくつあるか求めてください。
ただし、答えは非常に大きくなる可能性があるので、 10**9+7 で割った余りを出力してください。

制約
1≤S≤2000
入力はすべて整数
"""
mod = (10 ** 9 + 7)
tot = 1
l = [1, 0, 0]
for i in range(3, 2000):
  nex = (tot - l[-1] - l[-2]) % mod
  tot = (tot + nex) % mod
  l.append(nex)

print(l[int(input())])

# ==========================
# === E - Dist Max
# ==========================
"""問題文
二次元平面上に N 個の点があり、i 番目の点の座標は (xi,yi) です。 同じ座標に複数の点があることもあります。 
異なる二点間のマンハッタン距離として考えられる最大の値はいくつでしょうか。
ただし、二点 (xi,yi) と (xj,yj) のマンハッタン距離は |xi−xj|+|yi−yj| のことをいいます。

制約
2≤N≤2×10**5
1≤xi,yi≤10**9
入力はすべて整数
"""
N = int(input())
xy = [list(map(int, input().split())) for i in range(N)]
z = [x + y for x, y in xy]
w = [x - y for x, y in xy]

print(max(max(z) - min(z), max(w) - min(w)))
