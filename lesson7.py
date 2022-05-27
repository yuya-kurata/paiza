
# 提出 ※連想配列
N, K = map(int, input().split())

students = {}

for _ in range(N):
    key, value = map(str, input().split())
    students.setdefault(key, value)

for _ in range(K):
    l = input().split()
    
    list_count = len(l)
    method = l[0]
    student_number = l[1]

    if list_count == 2:
      if method == 'call':
         print(students[student_number])
      elif method == 'leave':
         del students[student_number]
    elif list_count == 3:
      student_name = l[2]
      students.setdefault(student_number,student_name)

# 解答１ ※連想配列
# 全ての生徒の出席番号と ID をセットで保持し、出席番号が与えられたら全ての出席番号の中から、その出席番号を探す方針のプログラムを組んだ場合、ループが最大で (100,000)^2 # 回回ってしまうため、実行時間制限に間に合いません。
# また、生徒の追加や削除のごとに生徒に対応する要素番号が変化するため、情報の管理が大変になってしまいます。
# これらの問題を解決するために連想配列というものを使うことにします。

# 連想配列とは、キーと呼ばれる値とそれに対応する値からなるデータ構造であり、N 個のキーとその値の組の中から、特定のキーに対応する値を取得する際にかかる時間が O(log N) # でおこなうことができます。
# また、連想配列ではキーと値の組の追加・削除も O(log N) でおこなうことができるため、今回の問題で与えられる全てのイベントの処理を O(log N) でおこなうことができるため、# この問題を O(K log (N + K)) で解くことができるようになります。
N, K = map(int, input().split())
roster = {x: y for x, y in [input().split() for _ in range(N)]}

for _ in range(K):
    s = input().split()
    if s[0] == "join":
        num, ID = s[1:]
        roster[num] = ID
    elif s[0] == "leave":
        num = s[1]
        del roster[num]
    else:
        num = s[1]
        print(roster[num])

# 解答確認後、修正
N, K = map(int, input().split())

students = {}

for _ in range(N):
    key, value = map(str, input().split())
    students.setdefault(key, value)

for _ in range(K):
    l = input().split()
    
    list_count = len(l)
    method = l[0]
    student_number = l[1]

    if method == 'call':
        print(students[student_number])
    elif method == 'leave':
        del students[student_number]
    else:
        student_name = l[2]
        students.setdefault(student_number,student_name)
