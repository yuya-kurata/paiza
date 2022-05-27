
# 提出 ※ N = 企業数, K = 取引数
N, K = map(int, input().split())

company_list = [] 

for index in range(N):
  company_list.append([])
  company_name, security_number, balance = map(str, input().split())
  company_list[index].append(company_name)
  company_list[index].append(security_number)
  company_list[index].append(balance)

for index_action in range(K):
    
    company_name, security_number, balance = map(str, input().split())
    
    for index in range(N):
        if company_name == company_list[index][0]:
            if security_number == company_list[index][1]:
                company_list[index][2] = int(company_list[index][2]) - int(balance)
            else:
                continue
        else:
            continue

for index in range(N):
    print(str(company_list[index][0]) + ' ' + str(company_list[index][2]))
            

# 提出後、修正 ※ N = 企業数, K = 取引数

# 決まった値から関連した値を取り出したい時には連想配列を使うと便利です。
# 連想配列では、上の 2 つの処理と要素の追加をいずれも O(log N) でおこなうことができるので、連想配列を用いることでこの問題を解くことができます。
# 最後に、与えられた順で会社の残高を出力する必要があるので、与えられた順に会社の名前を保持しておく必要があることに注意しましょう。
N, K = map(int, input().split())

data = {}
for _ in range(N):
    c, p, d = input().split()
    data[c] = (p, int(d))

for _ in range(K):
    g, m, w = input().split()

    pin, save = data[g]
    if pin != m:
        continue

    data[g] = (pin, save - int(w))

for name, d in data.items():
    print(name, d[1])

# 提出後、改善点
# 1. データ構造（２次元配列で持つのではなく、連想配列 + タプルで持つべき）
#   そうすることで、２重ループすることなく処理実行することができる。