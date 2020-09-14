"""
难度系数：***

2,3,5,7,11,13,…是素数序列。
类似：7,37,67,97,127,157 这样完全由素数组成的等差数列，叫等差素数数列。
上边的数列公差为30，长度为6。

2004年，格林与华人陶哲轩合作证明了：存在任意长度的素数等差数列。
这是数论领域一项惊人的成果！

有这一理论为基础，请你借助手中的计算机，满怀信心地搜索：

长度为10的等差素数列，其公差最小值是多少？

注意：需要提交的是一个整数，不要填写任何多余的内容和说明文字。
"""


def init_num():
    global tot
    for i in range(2, N):
        if dp[i] == 1:
            continue
        prim[tot] = i  # 记录N以内的所有素数
        tot += 1
        j = i
        while i * j < N:
            dp[i * j] = 1  # 不是素数的位置标记1
            j += 1


def get_dif():
    global dif
    init_num()

    # print(dp[:100])
    # print(prim[:100])

    # print(tot)

    while dif * 10 < N:
        for j in range(tot):
            flag, temp = True, prim[j]
            for k in range(1, 10):  # temp后边是否再有9个满足等差条件的素数
                if temp + dif >= N or dp[temp + dif] == 1:
                    flag = False
                    break
                else:
                    temp += dif
            if flag:
                # print(dif, prim[j])
                return dif
        dif += 1


N = 1000010
dp = [1, 1] + [0] * N
tot = 0
dif = 1
prim = [0] * N

if __name__ == '__main__':
    # print(is_prime(2))
    print(get_dif())

