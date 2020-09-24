def init(n):
    for i in range(1, n+1):
        pre[i] = i


def find_pre(key):
    """找key的根，也就是找带头大哥"""
    if pre[key] == key:
        return key
    else:
        pre[key] = find_pre(pre[key])  # 如果当前节点不是根节点，就找当前节点的父节点的根节点。最后的到的根就是key的根
    return pre[key]


def unite(x, y):
    """如果x和y不相连则连接它们，即x的根和y的根不同，则让一方从属于另一方"""
    rootx = find_pre(x)
    rooty = find_pre(y)
    if rootx != rooty:
        pre[rootx] = rooty


m, n = list(map(int, input().split()))
line = int(input())
ans = 0
lst = [0 for i in range(m*n+1)]
pre = [0 for i in range(m*n+1)]  # 存放以索引值为节点序号的点的根节点
init(m*n)  # 初始化每个节点的根节点都为它自己，即开始时都各不相连
for i in range(line):
    x, y = list(map(int, input().split()))
    unite(x, y)  # 每输入两个有关联的节点，就让他们相连
for i in range(1, m*n+1):
    lst[find_pre(i)] = 1  # 遍历每个节点，把她们对应的根节点的索引位置赋值1，比如节点1的老大是13，5的老大也是13，则他们属于1个节点集，操作和都只能将lst的13索引的地方赋值1
for i in range(1, m*n+1):  # 等于1的个数就是最后的子集个数
    if lst[i] == 1:
        ans += 1
print(ans)
