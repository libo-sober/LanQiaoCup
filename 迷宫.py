"""
下图给出了一个迷宫的平面图，其中标记为 1 的为障碍，标记为 0 的为可 以通行的地方。
010000
000100
001001
110000
迷宫的入口为左上角，出口为右下角，在迷宫中，只能从一个位置走到这 个它的上、下、左、右四个方向之一。
对于上面的迷宫，从入口开始，可以按DRRURRDDDR 的顺序通过迷宫， 一共 10 步。其中 D、U、L、R
分别表示向下、向上、向左、向右走。 对于下面这个更复杂的迷宫（30 行 50 列），请找出一种通过迷宫的方式，
其使用的步数最少，在步数最少的前提下，请找出字典序最小的一个作为答案。
 请注意在字典序中D<L<R<U。
 （如果你把以下文字复制到文本文件中，请务 必检查复制的内容是否与文档中的一致。
 在试题目录下有一个文件 maze.txt， 内容与下面的文本相同）

 这是一道结果填空的题，你只需要算出结果后提交即可。本题的结果为一 个字符串，
 包含四种字母 D、U、L、R，在提交答案时只填写这个字符串，填 写多余的内容将无法得分.
"""


class Node(object):
    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.c = c

    def __str__(self):
        return self.c


def up(node):
    return Node(node.x - 1, node.y, node.c + 'U')


def down(node):
    return Node(node.x + 1, node.y, node.c + 'D')


def left(node):
    return Node(node.x, node.y - 1, node.c + 'L')


def right(node):
    return Node(node.x, node.y + 1, node.c + 'R')


if __name__ == '__main__':
    m = 0
    n = 0
    visited = set()
    map_int = []
    queen = []
    with open('maze', mode='r', encoding='utf-8') as fp:
        data = fp.readlines()
        for line in data:
            map_int.append(list(line.strip()))
        m = len(map_int)
        n = len(map_int[0])
        node = Node(0, 0, '')
        queen.append(node)
        while len(queen) != 0:
            move_node = queen[0]
            queen.pop(0)
            move_str = str(move_node.x) + ' ' + str(move_node.y)
            if move_str not in visited:
                visited.add(move_str)
                if move_node.x == m - 1 and move_node.y == n - 1:
                    print(move_node)
                    print(len(move_node.__str__()))
                    break
                if move_node.x < m - 1 and map_int[move_node.x + 1][move_node.y] == '0':
                    queen.append(down(move_node))
                if move_node.y > 0 and map_int[move_node.x][move_node.y - 1] == '0':
                    queen.append(left(move_node))
                if move_node.y < n - 1 and map_int[move_node.x][move_node.y + 1] == '0':
                    queen.append(right(move_node))
                if move_node.x > 0 and map_int[move_node.x - 1][move_node.y] == '0':
                    queen.append(up(move_node))

"""
广度搜索，最先到满足结束条件的肯定是最短的那一个路径.
"""




