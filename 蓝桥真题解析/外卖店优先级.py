class Order:
    """存放信息"""
    def __init__(self, ts, id):
        self.ts = ts
        self.id = id


def main():
    n, m, t = list(map(int, input().split()))
    info = []
    cash = []
    score = [0 for i in range(n+1)]
    for i in range(m):
        ts, id_ = list(map(int, input().split()))
        info.append(Order(ts, id_))
    # info.sort(key=lambda order: order.ts)
    for i in range(1, t+1):
        flag = True
        for data in info:
            if data.ts == i:
                # 对应店铺有订单，加上2
                score[data.id] += 2
                for s in score:
                    # 没有订单的店铺-1，等于0的不用变化
                    if score.index(s) == data.id:
                        continue
                    elif s == 0:
                        continue
                    score[score.index(s)] -= 1
                # info.remove(data)
                flag = False
        else:
            # 如果在一个时刻两家都没有订单，都-1
            if flag:
                for s in score:
                    if s == 0:
                        continue
                    score[score.index(s)] -= 1
        for s in score:
            # 某一时刻结束后，根据每个店铺的积分，决定改店铺是去是留
            if s > 5:
                cash.append(score.index(s))
            if s <= 3:
                if score.index(s) in cash:
                    cash.remove(score.index(s))
    print(len(cash))  # 打印缓冲区内的店铺个数


if __name__ == '__main__':
    main()

"""
2 6 6
1 1
5 2
3 1
6 2
2 1
6 2
"""
