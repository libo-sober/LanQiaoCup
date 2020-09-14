"""
6x6的方格，沿着格子的边线剪开成两部分。
要求这两部分的形状完全相同。

如图：p1.png, p2.png, p3.png 就是可行的分割法。

试计算：
包括这3种分法在内，一共有多少种不同的分割方法。
注意：旋转对称的属于同一种分割法。

请提交该整数，不要填写任何多余的内容或说明文字。
"""


def dfs(x, y):
    global ans
    if x == 0 or x == n or y == 0 or y == n:
        ans += 1
        return

    for i in range(4):
        tx = x + directions[i][0]
        ty = y + directions[i][1]
        if arr_map[tx][ty] == 0:
            arr_map[tx][ty] = 1
            arr_map[n - tx][n - ty] = 1
            dfs(tx, ty)
            arr_map[tx][ty] = 0
            arr_map[n - tx][n - ty] = 0

    return ans / 4


n = 6
ans = 0
arr_map = [[0] * (n + 1) for i in range(10)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
arr_map[3][3] = 1
# print(arr_map)

if __name__ == '__main__':
    print(dfs(n // 2, n // 2))  # 509
    # print(ans)

"""
注释：
从中心带你（3，3）开始出发，两边对称走，最后总数要除以4
"""
