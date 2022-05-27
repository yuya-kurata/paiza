
# 提出
N, K = map(int, input().split())

data = {}

for _ in range(N):
    department = str(input())
    data.setdefault(department, {})

for _ in range(K):
    department_name, order_number, amount_money = input().split()
    data[department_name][order_number] = amount_money

for key in data.keys():


    print(key)
    
    for key,value in data[key].items():
        print(str(key) + ' ' + str(value))
    
    print('-----')


# 解答
# 決まった値から関連した値を取り出したい時には連想配列を使うと便利です。
# 今回の問題では、「初めに与えられる情報」と「領収書に含まれる情報」のうち共通しているものは部署名であるので、キ# ーを「部署名」・値を「注文番号と金額をペアで保持する配列」とすれば良いです。
# 連想配列では、「キーから値を取り出す操作」と「キーと値の追加」をいずれも O(log N) でおこなうことができるので、# 連想配列を用いることでこの問題を解くことができます。
# 最後に、与えられた順で部署の残高を出力する必要があるので、与えられた順に部署の名前を保持しておく必要があること# に注意しましょう。

N, K = map(int, input().split())
departments = {input(): [] for _ in range(N)}

for _ in range(K):
    a, p, m = input().split()

    departments[a].append((p, m))

for key, val in departments.items():
    print(key)
    for p, m in val:
        print(p, m)

    print("-----")
            