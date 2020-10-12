# 处理组合问题


import copy
class Candy:
    def __init__(self, taste):
        self.taste = taste


def find(candies, m):
    res = []
    collection = set()
    ans = 1
    while True:
        for r in res:
            if len(r) == m:
                return
        collection.add(*candies[-1].taste)
        res.append(collection)
        candies.pop()
        for candy in candies:
            for r in res:
                r.add(candy.taste)
        ans += 1


def main():
    n, m, k = list(map(int, input().split()))
    candies = []
    for i in range(n):
        taste = list(map(int, input().split()))
        candies.append(Candy(taste))
    find(candies, m)


if __name__ == '__main__':
    main()


"""
6 5 3
1 1 2
1 2 3
1 1 3
2 3 5
5 4 2
5 1 2
"""
