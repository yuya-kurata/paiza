
# 提出 ※連想配列
N, K = map(int, input().split())
students = {}

for i in range(N):
    key, value= map(str, input().split())
    students.setdefault(key, value)
    
for k in range(K):
    student_number = str(input())
    print(students[student_number])

# 解答
N, K = map(int, input().split())
roster = {(x, y) for x, y in [input().split() for _ in range(N)]}

for _ in range(K):
    q = input()
    for num, ID in roster:
        if num == q:
            print(ID)
