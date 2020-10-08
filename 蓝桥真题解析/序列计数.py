"""
【问题描述】
小明想知道，满足以下条件的正整数序列的数量：
1. 第一项为 n；
2. 第二项不超过 n；
3. 从第三项开始，每一项小于前两项的差的绝对值。
请计算，对于给定的 n，有多少种满足条件的序列。
【输入格式】
输入一行包含一个整数 n。
【输出格式】
输出一个整数，表示答案。答案可能很大，请输出答案除以10000的余数。
【样例输入】
4
【样例输出】
7
【样例说明】
以下是满足条件的序列：
4 1
4 1 1
4 1 2
4 2
4 2 1
4 3
4 4
【评测用例规模与约定】
对于 20% 的评测用例，1 <= n <= 5；
对于 50% 的评测用例，1 <= n <= 10；
对于 80% 的评测用例，1 <= n <= 100；
对于所有评测用例，1 <= n <= 1000。
"""
# def func(a, b):
#     global ans
#     res = 1
#     while res < abs(a - b):
#         func(b, res)
#         res += 1
#     ans += 1
#
# n = int(input())
# ans = 0
# for i in range(1, n+1):
#     func(n, i)
# print(ans)
import sys
sys.setrecursionlimit(10000)
def dfs(old, now):
    if now <= 0:
        return 0
    if hx[old][now] != 0:
        return hx[old][now]
    hx[old][now] = (1 + dfs(old, now - 1) + dfs(now, abs(old - now) - 1)) % 10000
    return hx[old][now]

n = int(input())
hx = [[0] * (n+1) for i in range(n+1)]
print(dfs(n, n))
print(hx)

