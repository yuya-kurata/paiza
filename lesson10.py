
# 提出
N, K = map(int, input().split())

members = []
events = []

# メンバー一覧取得 
for _ in range(N):
  member_name = str(input())
  members.append(member_name)

# event判定
for _ in range(K):
    
    members = sorted(members)
    event = input().split() 
    
    if event[0] == 'handshake':
         for name in members:
             print(name)
    
    elif event[0] == 'leave':
        members.remove(event[1])
        
    elif event[0] == 'join':
        members.append(event[1])

##
# 解答
## 

# イベントが最大で 100,000 回与えられることを踏まえると、実行時間制限に間に合う目安の計算回数である 10^8 以下に全体の計算量を抑えるためには、各イベントの処理「アイドル# の加入」「アイドルの脱退」をO(log N) 程度の計算量で抑える必要があります。
# これらを満たすデータ構造として順序付集合が挙げられます。これは N 要素の集合への要素の追加・削除を O(log N) でおこなうことができ、要素を常にソートされた状態で保持しま# す。
# 各言語によって順序付集合の仕様は異なるので詳しい実装は言語ごとの実装例をみてください。入力に応じた順序付集合の処理を行うことでこの問題を解くことができます。

# set オブジェクトを使います。
# set オブジェクトの要素は set.remove(削除したい要素) のように remove メソッド# を使うことで削除できます。
# set オブジェクトの remove メソッドの計算量は平均 O(1) です。

N, K = map(int, input().split())
names = {input() for _ in range(N)}

for _ in range(K):
    event = input()

    if event == "handshake":
        for name in sorted(names):
            print(name)
    else:
        event, name = event.split()
        if event == "join":
            names.add(name)
        else:
            names.remove(name)


# 解答後、修正
# 提出
N, K = map(int, input().split())

events = []

# メンバー一覧取得 
members = {input() for _ in range(N)}

# event判定
N, K = map(int, input().split())

# メンバー一覧取得 
members = {input() for _ in range(N)}

# event判定
for _ in range(K):
    
    event = input().split() 
    
    if event[0] == 'handshake':
         for name in sorted(members):
             print(name)
    
    elif event[0] == 'leave':
        members.remove(event[1])
        
    elif event[0] == 'join':
        members.add(event[1])


