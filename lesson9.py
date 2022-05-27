
# 提出
N, K, P  = map(int, input().split())

students = [int(input()) for _ in range(N)]
events = {}

for _ in range(K):
  event = input().split()
  
  if event[0] == 'join':
      students.append(int(event[1]))
  
  elif event[0] == 'sorting':
      students = sorted(students)
      
      # paiza君の身長判定
      for index, height in enumerate(students):
          if P < height:
              students.insert(index, P)
              print(students.index(P) + 1)
              break

# 解答
N, K, P = map(int, input().split())
A = [int(input()) for _ in range(N)]

A.append(P)
ans = sorted(A).index(P) + 1

for _ in range(K):
    event = input()

    if event == "sorting":
        print(ans)
        continue

    x = int(event.split()[1])
    if x < P:
        ans += 1
