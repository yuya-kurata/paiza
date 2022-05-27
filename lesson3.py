###
# 指定要素の検索
###

# 提出
Q, K = map(int, input().split())

Q_arrangements = [int(input()) for _ in range(Q)]
K_arrangements = [int(input()) for _ in range(K)]


for _ in K_arrangements:
    
    judge = Q_arrangements.count(_)
    
    if judge:
        print("YES")
    else:
        print("NO")

# 解答 ※setオブジェクトを使用
# set はハッシュ法を用いて値を管理しているため、in 演算子による値の探索が平均 O(1) で実行できます
N, Q = map(int, input().split())
A = {int(input()) for _ in range(N)}

for _ in range(Q):
    k = int(input())
    if k in A:
        print("YES")
    else:
        print("NO")


# 解答確認後、修正
Q, K = map(int, input().split())

Q_arrangements = {int(input()) for _ in range(Q)}

for _ in range(K):
    
    judge = int(input())
    
    if judge in Q_arrangements:
        print("YES")
    else:
        print("NO")
