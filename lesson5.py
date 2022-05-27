
# 提出
N, K = map(int, input().split())

A = [int(input()) for _ in range(N)]

for i in range(K):
    
    pop_or_show = input()
    
    if pop_or_show == 'pop':
        A.pop(0)
    else:
        for k in A:
            print(k)

# 解答1 ※deque オブジェクトの popleft メソッドの計算量は O(1) です。 ※両端キュー
# https://note.nkmk.me/python-collections-deque/
# https://pg-chain.com/python-queue
# http://www.physics.okayama-u.ac.jp/~otsuki/lecture/CompPhys2/string/container.html

from collections import deque

N, K = map(int, input().split())
A = deque([int(input()) for _ in range(N)])

f = 0
for _ in range(K):
    s = input()
    if s == "pop":
        A.popleft()
        continue
    for a in A:
        print(a)

# 解答2
N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

f = 0
for _ in range(K):
    s = input()
    if s == "pop":
        f += 1
        continue
    for i in range(f, N):
        print(A[i])