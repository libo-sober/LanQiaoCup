"""
给定一棵包含 N 个节点的完全二叉树，树上每个节点都有一个权值，
按从上到下、从左到右的顺序依次是 A1, A2, · · · AN，如下图所示：

现在小明要把相同深度的节点的权值加在一起，他想知道哪个深度的节点权值之和最大？
如果有多个深度的权值和同为最大，请你输出其中最小的深度。

注：根的深度是 1。

第一行包含一个整数 N。
第二行包含 N 个整数 A1, A2, · · · AN 。

输出一个整数代表答案

7
1 6 5 4 3 2 1

2
"""


def get_deep():
    n = int(input())
    lst = list(map(int, input().split()))
    deep = 1
    while 2 ** deep - 1 <= n:
        lst[deep - 1] = sum(lst[2 ** (deep - 1) - 1:2 ** deep - 1])
        deep += 1
    if 2 ** (deep - 1) - 1 < n:
        lst[deep - 1] = sum(lst[2 ** (deep - 1) - 1:])
    return lst.index(max(lst)) + 1


if __name__ == '__main__':
    print(get_deep())


"""
注释：
1. map(int, input().split())  
    这产生的是一个生成器， next一次会得到一个值
    list可以全部结收生成器中的值并返回一个列表
    gen = map(int, input().split())
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    
    1 6 5 4 3 2 1
    1
    6
    5
    4
    3
2. 完全二叉树的特性
    每一层的结点数：2 ** deep
    满二叉树的总结点数：2 ** deep - 1
3. lst.index(a)
    返回值为列表中最先出现a的索引值
    加1后在此就是a对应的最小深度
"""

