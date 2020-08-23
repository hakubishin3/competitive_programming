# ==========================
# === A - Takoyaki
# ==========================
"""
問題文
高橋君はたこ焼きが好きです。
たこ焼き器を使うと、1 度に最大で X 個のたこ焼きを作ることができます。
これにかかる時間は作る個数によらず T 分です。
N 個のたこ焼きを作るためには何分必要ですか？

制約
1≤N,X,T≤1000
入力は全て整数
"""
N, X, T = map(int, input().split())

times = (N + X - 1) // X   # 切り上げ
print(times * T)

# ==========================
# === B - Multiple of 9
# ==========================
"""
問題文
整数 N が 9 の倍数であることと、N を十進法で表したときの各桁の数の和が 9 の倍数であることは同値です。
N が 9 の倍数であるか判定してください。

制約
0≤N<10**200000
N は整数
"""
N = list(map(int, list(input())))

if sum(N) % 9 == 0:
  print("Yes")
else:
  print("No")

# ==========================
# === C - Step
# ==========================
"""
問題文
N 人が 1 列に並んでおり、前から i 番目の人の身長は Ai です。
それぞれの人の足元に、高さが 0 以上の踏み台を設置し、全ての人が次の条件を満たすようにしたいです。
条件：踏み台を込めて身長を比較したとき、自分より前に、自分より背の高い人が存在しないこの条件を満たす時の、踏み台の高さの合計の最小値を求めてください。

制約
1≤N≤2×10**5
1≤Ai≤10**9
入力は全て整数
"""
N = int(input())
A = list(map(int, input().split()))

res = 0
max_size = A[0]
for i in range(N):
  # max_sizeを使い回すことで計算を抑える
  max_size = max(max_size, A[i])
  res += max_size - A[i]

print(res)

# ==========================
# === E - Bomber
# ==========================
"""
問題文
H×W マスの二次元グリッドがあります。この中には M 個の爆破対象があります。 
i 個目の爆破対象の位置は (hi,wi)です。
高橋君は 1 つのマスを選び、そのマスに爆弾を設置し、起爆します。爆弾と同じ行または同じ列に存在する爆破対象が爆破されます。
爆破対象が存在するマスに爆弾を設置することも出来ます。高橋君は、爆破する爆破対象の数を最大化しようとしています。最大でいくつの爆破対象を爆破出来るか答えてください。

制約
入力は全て整数
1≤H,W≤3×10**5
1≤M≤min(H×W,3×10**5)
1≤hi≤H
1≤wi≤W
(hi,wi)≠(hj,wj)(i≠j)
"""
import sys
input = sys.stdin.readline
 
H, W, M = map(int, input().split())
Hsum = [0] * H
Wsum = [0] * W
hw = set()
for m in range(M):
  h, w = map(lambda x: int(x) - 1, input().split())
  Hsum[h] += 1
  Wsum[w] += 1
  hw.add((h, w))

mh = max(Hsum)
mw = max(Wsum)
hidx = [i for i, _ in enumerate(Hsum) if _ == mh]
widx = [i for i, _ in enumerate(Wsum) if _ == mw]

if len(hidx) * len(widx) > M:
  print(mh + mw)
else:
  fi_flg = False
  for h in hidx:
    for w in widx:
      if (h, w) not in hw:
        print(mh + mw)
        fi_flg = True
        break
    if fi_flg:
      break
  if fi_flg is False:
    print(mh + mw - 1)
