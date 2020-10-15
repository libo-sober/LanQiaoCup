"""
 题目描述
到x星球旅行的游客都被发给一个整数，作为游客编号。
x星的国王有个怪癖，他只喜欢数字3,5和7。
国王规定，游客的编号如果只含有因子：3,5,7,就可以获得一份奖品。
前10个幸运数字是：3 5 7 9 15 21 25 27 35 45，因而第11个幸运数字是：49
小明领到了一个幸运数字 59084709587505。
去领奖的时候，人家要求他准确说出这是第几个幸运数字，否则领不到奖品。
请你帮小明计算一下，59084709587505是第几个幸运数字。
输出
输出一个整数表示答案
"""
# def is_lucky(num):
#     while num != 1:
#         for i in [3, 5, 7]:
#             if num % i == 0:
#                 num = num // i
#                 break
#         else:
#             return False
#
#     return True
#
#
# ans = 0
#
# for i in range(2, 59084709587505):
#     if is_lucky(i):
#         ans += 1
#
# print(ans)
# 生成法
MAX = 59084709587505
# MAX = 49
a = [3, 5, 7]
s = set()
tou = 1
while True:
    for i in a:
       t = tou * i
       if t <= MAX:
        s.add(t)
    lst = sorted(s)
    for i in lst:
        if i > tou:
            tou = i
            break
    if tou >= MAX:
        break
# print(lst)
print(len(s))  # 1905
