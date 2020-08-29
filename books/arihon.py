# ==========================
# === 部分和問題
# ==========================
"""
問題文
整数 a1, a2, ... anが与えられます.
その中からいくつか選び, その和をちょうどkにすることができるかを判定しなさい.

制約
1≤n≤20
-10**8≤ai≤10**8
-10**8≤k≤10**8
"""
def dfs(i: int, sum: int) -> bool:
  # n個決め終わったら, 残りi以降を調べる
  if i == n:
    return sum == k

  # a[i]を使わない場合
  if dfs(i + 1, sum):
    return True

  # a[i]を使う場合
  iff dfs(i + 1, sum + a[i]):
    return True

  return False


n, k = map(int, input().split())
a = list(map(int, input().split()))

if dfs(0, 0):
  print("Yes")
else:
  print("No")
