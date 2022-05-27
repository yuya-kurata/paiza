###
# 指定要素の検索
###

# 提出
arrangements_count, judge_number = map(int,input().split())

count = 0

for i in range(arrangements_count):
    
    count += 1
    
    input_number = int(input())
    
    if judge_number == input_number:
        print("YES")
        break
    elif arrangements_count == count:
        print("NO")
        break
      

# 解答
N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

exist = False
for a in A:
    if a == K:
        exist = True
        break

print("YES" if exist else "NO")


# 解答確認後、修正
arrangements_count, judge_number = map(int,input().split())

count = 0

for i in range(arrangements_count):
    
    exist = False
    input_number = int(input())
    
    if judge_number == input_number:
        exist = True
        break
  
print("YES" if exist else "NO")