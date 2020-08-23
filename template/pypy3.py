# ==========================
# === 入力
# ==========================
# input()を早くする
import sys
input = sys.stdin.readline

# 整数 1 つ
N = int(input())

# 整数複数個
N, K = map(int, input().split())

# 整数 N 個 (スペース区切り)
A = list(map(int, input().split()))

# 整数 N 個 (改行区切り)
L = [int(input()) for i in range(N)]

# 整数 (縦 H 横 W の行列)
S = [list(map(int, input().split())) for i in range(H)]


# ==========================
# === 標準出力
# ==========================
# リストをスペース区切りで出力
arr = [1, 2, 3]
print(*arr)

# リストを改行区切りで出力
arr = [1, 2, 3]
print(*arr, sep="\n")

# 最後に改行を入れない出力
print("あああ", end="")


# ==========================
# === 処理の終了
# ==========================
exit()


