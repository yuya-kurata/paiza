###
# 指定の位置への要素の追加
###

# 提出
arrangements = []
premise = input().split(' ')

arrange_count = int(premise[0])
insert_count = int(premise[1])
insert_number = int(premise[2])

for i in range(arrange_count):
    
    number = int(input())
    arrangements.append(number)
    
    if insert_count == i + 1:
        arrangements.append(insert_number)

for i in arrangements:
    print(i)


# 解答
# 指定の位置への要素の追加（insertメソッド 計算量：O(N)）
N, K, Q = map(int, input().split())
A = [int(input()) for _ in range(N)]

A.insert(K, Q)

for a in A:
    print(a)