"""
问题描述
       由1对括号，可以组成一种合法括号序列：()。
　　由2对括号，可以组成两种合法括号序列：()()、(())。
　　由4对括号组成的合法括号序列一共有多少种？
"""

"""
第一种方法：手算。
深度为1的：() () () ()   1
深度为2的：(()) () (), () (()) (), () () (()), (()) (()), (()()) (), () (()()), (()()())  7
深度为3的：((()) (), () ((())), (()(())), ((())()), ((()())) 5
深度为4的：(((()))) 1
1+7+5+1 = 14
"""


# 第二种方法：代码。
def match(left, right):
    global n, ans
    if left == n:
        ans += 1
        return
    match(left + 1, right)
    if left > right:
        match(left, right + 1)


def get_num():
    global ans,n
    match(0, 0)
    return ans


n = 4
ans = 0

if __name__ == '__main__':
    print(get_num())  # 14
