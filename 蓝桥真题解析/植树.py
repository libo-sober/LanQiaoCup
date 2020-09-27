"""
【问题描述】
小明和朋友们一起去郊外植树，他们带了一些在自己实验室精心研究出的小树苗。
小明和朋友们一共有 n 个人，他们经过精心挑选，在一块空地上每个人挑选了一个适合植树的位置，总共 n 个。他们准备把自己带的树苗都植下去。
然而，他们遇到了一个困难：有的树苗比较大，而有的位置挨太近，导致两棵树植下去后会撞在一起。
他们将树看成一个圆，圆心在他们找的位置上。如果两棵树对应的圆相交，这两棵树就不适合同时植下（相切不受影响），称为两棵树冲突。
小明和朋友们决定先合计合计，只将其中的一部分树植下去，保证没有互相冲突的树。他们同时希望这些树所能覆盖的面积和（圆面积和）最大。
【输入格式】
输入的第一行包含一个整数 n ，表示人数，即准备植树的位置数。
接下来 n 行，每行三个整数 x, y, r，表示一棵树在空地上的横、纵坐标和半径。
【输出格式】
输出一行包含一个整数，表示在不冲突下可以植树的面积和。由于每棵树的面积都是圆周率的整数倍，请输出答案除以圆周率后的值（应当是一个整数）。
【样例输入】
6
1 1 2
1 4 2
1 7 2
4 1 2
4 4 2
4 7 2
【样例输出】
12
【评测用例规模与约定】
对于 30% 的评测用例，1 <= n <= 10；
对于 60% 的评测用例，1 <= n <= 20；
对于所有评测用例，1 <= n <= 30，0 <= x, y <= 1000，1 <= r <= 1000。
"""
import math


class Circle:
    """存储每颗树的位置信息，和它的覆盖面积，并提供判断自身与另一颗树的覆盖范围的位置关系"""
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.absolute_area = r ** 2

    def judge_relation(self, *args):
        """
        判断两圆之间的关系
        @args:多值参数
        """
        if args:  # args（这里的args就是一个元组）不为空时
            flag = [False for i in range(len(args))]
            i = 0
            for circle in args:
                dis = math.sqrt((self.x - circle.x) ** 2 + (self.y - circle.y) ** 2)
                if self.r + circle.r < dis or self.r + circle.r == dis:  # 外离和外切
                    """若两个圆属于外切和外离的情况，置flag[i]为真"""
                    flag[i] = True
                i += 1
            return flag
        else:
            # args为空，第一颗树，肯定不会存在与其他树的位置关系情况，直接返回一个元组，因为后边的all()的参数必须为可迭代对象
            return [True, ]


class PlantTree:
    def __init__(self, n):
        self.n = n  # 待植的树的棵数
        self.tree = [0 for i in range(n)]  # 存放每一颗树的位置信息
        self.vis = []  # 存放已经种植的树
        self.total_area = 0  # 已经种植的树覆盖的总面积

    def init(self):
        for i in range(self.n):
            x, y, r = list(map(int, input().split()))
            self.tree[i] = Circle(x, y, r)
        self.tree.sort(key=lambda circle: circle.r, reverse=True)  # 半径从大到小排序，覆盖面积最大的先种

    def plant(self):
        for i in range(self.n):
            # flag = all(self.tree[i].judge_relation(*self.vis))
            if all(self.tree[i].judge_relation(*self.vis)):
                """注意all()的参数必须是可迭代对象，vis是一个列表用*打散传入"""
                # 如果当前树与已种的树不会相交，则把此树放入已种树的列表。
                self.vis.append(self.tree[i])
                self.total_area += self.tree[i].absolute_area
        return self.total_area


def main():
    n = int(input())
    plant_tree = PlantTree(n)
    plant_tree.init()
    plant_tree.plant()
    print(plant_tree.total_area)


if __name__ == '__main__':
    main()





