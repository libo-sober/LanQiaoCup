# gen = map(int, input().split())
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# dif = 5
# new_dif = 8
# dif = new_dif if new_dif < dif else dif
# print(dif)
#
# lst = [1, 3, 5, 7, 9]
# print(min(lst), max(lst))

l1 = [22, 33, 1, 2, 7, 4]
# l2 = sorted(l1)
# print(l1, l2)

l1.sort()
print(l1)  # [1, 2, 4, 7, 22, 33] 返回值为None 把原来的列表元素从小到大排序，改变原列表内容
l2 = [('太白',18), ('alex', 73), ('wusir', 35), ('口天吴', 41)]
l2.sort(key=lambda x: x[1])
# print(l2)  # [('太白', 18), ('wusir', 35), ('口天吴', 41), ('alex', 73)]
l2.sort(key=lambda x: x[1], reverse=True)
print(l2)  # [('alex', 73), ('口天吴', 41), ('wusir', 35), ('太白', 18)]




