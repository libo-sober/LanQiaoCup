"""
【问题描述】
一个正整数如果任何一个数位不大于右边相邻的数位，则称为一个数位递增的数，例如1135是一个数位递增的数，而1024不是一个数位递增的数。
给定正整数 n，请问在整数 1 至 n 中有多少个数位递增的数？
【输入格式】
输入的第一行包含一个整数 n。
【输出格式】
输出一行包含一个整数，表示答案。
【样例输入】
30
【样例输出】
26
【评测用例规模与约定】
对于 40% 的评测用例，1 <= n <= 1000。
对于 80% 的评测用例，1 <= n <= 100000。
对于所有评测用例，1 <= n <= 1000000。
"""
import time

# 不要使用python内置的排序函数等，否则会超时
# n = int(input())

start = time.time()


def solve(num):
    pre = 9
    while num != 0:
        now = num % 10
        num = num // 10
        # 这里如果你数位分离后存入一个列表再对列表进行遍历比较大小则会造成时间超出1s
        # 因为遍历需要用到range函数
        # 如果你存入列表后用排序函数sorted得到一个新列表与原列表笔较是否相同也会超出1s
        if now <= pre:
            pre = now
        else:
            return False
    return True


count = 0

for i in range(1, 1000000+1):
    if solve(i):
        count += 1
print(count)

end = time.time()
print(end - start)
# n = 1000000 时间为0.34078240394592285s
