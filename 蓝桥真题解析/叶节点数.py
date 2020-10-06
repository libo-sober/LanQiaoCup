"""
【问题描述】
一棵包含有2019个结点的二叉树，最多包含多少个叶结点？
【答案提交】
这是一道结果填空的题，你只需要算出结果后提交即可。本题的结果为一个整数，在提交答案时只填写这个整数，填写多余的内容将无法得分。
"""


class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        else:
            print('空队列')

    def isEmpty(self):
        return self.items == []


class Tree:
    def __init__(self):
        self.root = None

    def addNode(self, item):
        node = Node(item)
        cur = self.root
        if cur is None:
            self.root = node
            return
        queue = Queue()
        queue.enqueue(cur)
        while not queue.isEmpty():
            nd = queue.dequeue()
            if nd.left is None:
                nd.left = node
                return
            else:
                queue.enqueue(nd.left)
            if nd.right is None:
                nd.right = node
                return
            else:
                queue.enqueue(nd.right)

    def travel(self):
        cur = self.root
        queue = Queue()
        queue.enqueue(cur)
        while not queue.isEmpty():
            nd = queue.dequeue()
            print(nd.item)
            if nd.left is not None:
                queue.enqueue(nd.left)
            if nd.right is not None:
                queue.enqueue(nd.right)

    def findLeaf(self):
        count = 0
        cur = self.root
        queue = Queue()
        queue.enqueue(cur)
        while not queue.isEmpty():
            nd = queue.dequeue()
            if nd.left is None and nd.right is None:
                count += 1
            else:
                if nd.left is not None:
                    queue.enqueue(nd.left)
                if nd.right is not None:
                    queue.enqueue(nd.right)
        return count


def main():
    n = 2019
    tree = Tree()
    for i in range(1, n+1):
        tree.addNode(i)
    # tree.travel()
    print(tree.findLeaf())


if __name__ == '__main__':
    main()  # 1010

