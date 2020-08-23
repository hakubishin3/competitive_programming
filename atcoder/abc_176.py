"""
A - Takoyaki

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


"""
B - Multiple of 9

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


"""
C - Step

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

