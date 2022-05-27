
###
# 先頭要素の削除
###
count = int(input())
sequences = []
delete_sequences = []

for i in range(count):
    
    if i == 0:
      delete_sequences.append(int(input()))
    else:
      print(int(input()))

# 解答1 ※del 文を list オブジェクトに用いたときの計算量は O(N) です。
N = int(input())
A = [int(input()) for _ in range(N)]

del A[0]

for a in A:
    print(a)

# 解答2
N = int(input())
A = [int(input()) for _ in range(N)]

for i in range(1, N):
    print(A[i])