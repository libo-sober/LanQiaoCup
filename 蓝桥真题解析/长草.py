"""
【问题描述】
小明有一块空地，他将这块空地划分为 n 行 m 列的小块，每行和每列的长度都为 1。
小明选了其中的一些小块空地，种上了草，其他小块仍然保持是空地。
这些草长得很快，每个月，草都会向外长出一些，如果一个小块种了草，则它将向自己的上、下、左、右四小块空地扩展，这四小块空地都将变为有草的小块。
请告诉小明，k 个月后空地上哪些地方有草。
【输入格式】
输入的第一行包含两个整数 n, m。
接下来 n 行，每行包含 m 个字母，表示初始的空地状态，字母之间没有空格。如果为小数点，表示为空地，如果字母为 g，表示种了草。
接下来包含一个整数 k。
【输出格式】
输出 n 行，每行包含 m 个字母，表示 k 个月后空地的状态。如果为小数点，表示为空地，如果字母为 g，表示长了草。
【样例输入】
4 5
.g...
.....
..g..
.....
2
【样例输出】
gggg.
gggg.
ggggg
.ggg.
【评测用例规模与约定】
对于 30% 的评测用例，2 <= n, m <= 20。
对于 70% 的评测用例，2 <= n, m <= 100。
对于所有评测用例，2 <= n, m <= 1000，1 <= k <= 1000。
"""
def grow_grass(x, y):
    for i in range(4):
        tx = x + direction[i][0]
        ty = y + direction[i][1]
        if 0 <= tx < n and 0 <= ty < m:
            if arr[tx][ty] == '.':
                arr[tx][ty] = 'g'
                map_arr[tx][ty] = 1


n, m = list(map(int, input().split()))
arr = [list(input()) for _ in range(n)]
k = int(input())
map_arr = []
direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]

for i in range(k):
    map_arr = [[0] * m for i in range(n)]
    for p in range(n):
        for q in range(m):
            if arr[p][q] == 'g' and map_arr[p][q] == 0:
                map_arr[p][q] = 1
                grow_grass(p, q)

for line in arr:
    print(*line, sep='')
