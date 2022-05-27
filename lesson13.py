
# 提出
count = int(input())

superchat_members = {}
join_members = []

for _ in range(count):
    event = input().split()
    
    if event[1] == 'give':
        superchat_members.setdefault(int(event[2]),event[0])
    elif event[1] == 'join':
        join_members.append(event[0])

superchat_members = sorted(superchat_members.items(), reverse=True)
for _ in range(len(superchat_members)):
    print(superchat_members[_][1])

join_members = sorted(join_members, reverse=False)
for _ in range(len(join_members)):
    print(join_members[_])

# 未解答