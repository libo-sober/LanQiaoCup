"""
标题：分数

1/1 + 1/2 + 1/4 + 1/8 + 1/16 + …
每项是前一项的一半，如果一共有20项,
求这个和是多少，结果用分数表示出来。
类似：
3/2
当然，这只是加了前2项而已。分子分母要求互质。

注意：
需要提交的是已经约分过的分数，中间任何位置不能含有空格。
请不要填写任何多余的文字或符号
"""


# def gcd(a, b):
#     while a % b != 0:
#         c = a % b
#         a = b
#         b = c
#     return c
#
#
# def get_num(n):
#     fenzi = 0
#     fenmu = 2 ** (n - 1)
#     for i in range(n):
#         fenzi += 2 ** i
#     mcf = gcd(fenmu, fenzi)
#
#     return f'{fenzi // mcf}/{fenmu // mcf}'
#
#
# if __name__ == '__main__':
#     print(get_num(20))  # 1048575/524288
#     # print(gcd(20, 35))  # 5

# 快速幂运算 这里只考虑正数次幂
def power(base, exp):
    res = 1
    while exp > 0:
        if exp & 1:  # 按位与 10的二进制  1010
            res *= base
        exp >>= 1  # 右移1位
        base *= base
    return res

# 最大公约数
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

a = power(2, 20)-1
b = power(2, 19)
c = gcd(a, b)
print(a//c, '/', b//c)
