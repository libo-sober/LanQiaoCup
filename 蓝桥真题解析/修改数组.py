n = int(input())
lst = list(map(int, input().split()))
new_lst = []

for item in lst:
    while item in new_lst:
        item += 1
    new_lst.append(item)

print(*new_lst)
