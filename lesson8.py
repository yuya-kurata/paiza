# 提出 ※連想配列
N, X, P  = map(int, input().split())

students = {}
X_height = int(X)
P_height = int(P)

students.setdefault(0, X_height)
students.setdefault(1, P_height)

for _ in range(2, N+2):
    
    student_height = int(input())
    students.setdefault(_, student_height)

student_height_sorted = sorted(students.values())
print(student_height_sorted.index(P) + 1)

# 解答1
N, X, P = map(int, input().split())
A = [int(input()) for _ in range(N)]

A.append(X)
A.append(P)
print(sorted(A).index(P) + 1)

# 解答確認後、修正
N, X, P  = map(int, input().split())

students = [int(input()) for _ in range(N)]
students.append(X)
students.append(P)

print(sorted(students).index(P) + 1)