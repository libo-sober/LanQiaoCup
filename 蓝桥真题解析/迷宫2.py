"""
X星球的一处迷宫游乐场建在某个小山坡上。
它是由10x10相互连通的小房间组成的。
房间的地板上写着一个很大的字母。
我们假设玩家是面朝上坡的方向站立，则：
L表示走到左边的房间，
R表示走到右边的房间，
U表示走到上坡方向的房间，
D表示走到下坡方向的房间。
X星球的居民有点懒，不愿意费力思考。
他们更喜欢玩运气类的游戏。这个游戏也是如此！
开始的时候，直升机把100名玩家放入一个个小房间内。
玩家一定要按照地上的字母移动。
迷宫地图如下：

UDDLUULRUL
UURLLLRRRU
RRUURLDLRD
RUDDDDUUUU
URUDLLRRUU
DURLRLDLRL
ULLURLLRDU
RDLULLRDDD
UUDDUDUDLL
ULRDLUURRR

请你计算一下，最后，有多少玩家会走出迷宫?
而不是在里边兜圈子。
请提交该整数，表示走出迷宫的玩家数目，不要填写任何多余的内容。
"""


def dfs(x, y):
    """
    深度搜索
    :param x: 位置横坐标
    :param y: 位置纵坐标
    :return: None
    """
    global ans
    while True:
        """所在（x, y）位置的人按照标识走出迷宫后推出循环"""
        # print(x, y)
        if x > 9 or x < 0 or y > 9 or y < 0:
            ans += 1
            # print(ans)
            break

        if data_map[x][y] == 1:
            break
        # 记录走过的位置
        data_map[x][y] = 1

        if data[x][y] == 'U':
            x -= 1

        elif data[x][y] == 'D':
            x += 1

        elif data[x][y] == 'L':
            # print(x, y)
            y -= 1

        elif data[x][y] == 'R':
            y += 1


def get_num():
    """
    获取走出迷宫的人数
    :return: 走出迷宫的人数
    """
    global data_map
    global ans
    for i in range(0, 10):
        for j in range(0, 10):
            """对每个位置进行遍历，注意每次遍历开始前要先对data_map清0"""
            # data_map = [[0] * 10] * 10  # 不要用这种方式定义，这样data_map[1][1] = 1 会导致每一行的第一个位置都为1
            data_map = [[0] * 10 for _ in range(10)]  # 这样行
            # print(i, j)
            dfs(i, j)

    return ans


def get_data(file_name):
    """
    获取数据
    :param file_name: 保存数据的文件
    :return: 获取的数据
    """
    data = []
    with open(file_name, mode='rt', encoding='utf-8') as f:
        for line in f:
            line = list(line.strip())
            data.append(line)
    return data


# data_map = [[0] * 10] * 10  # 不要用这种方式定义，这样data_map[1][1] = 1 会导致每一行的第一个位置都为1
data_map = [[0] * 10 for _ in range(10)]  # 这样行
# data_map = [[0 for _ in range(10)] for i in range(10)]  # 这样也行
# data_map = []
# for i in range(10):
#     data_map.append([0 for i in range(10)])
data = get_data('../数据/maze2')
ans = 0

if __name__ == '__main__':
    print(get_num())  # 31个人
    # dfs(8, 2)


