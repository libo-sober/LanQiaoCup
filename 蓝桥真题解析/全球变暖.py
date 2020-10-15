"""
 你有一张某海域NxN像素的照片，"."表示海洋、"#"表示陆地，如下所示：
.......
.##....
.##....
....##.
..####.
...###.
.......
其中"上下左右"四个方向上连在一起的一片陆地组成一座岛屿。例如上图就有2座岛屿。  
由于全球变暖导致了海面上升，科学家预测未来几十年，岛屿边缘一个像素的范围会被海水淹没。具体来说如果一块陆地像素与海洋相邻(上下左右四个相邻像素中有海洋)，它就会被淹没。  
例如上图中的海域未来会变成如下样子：
.......
.......
.......
.......
....#..
.......
.......

请你计算：依照科学家的预测，照片中有多少岛屿会被完全淹没。  

【输入格式】
第一行包含一个整数N。  (1 <= N <= 1000)  

以下N行N列代表一张海域照片。  

照片保证第1行、第1列、第N行、第N列的像素都是海洋。

【输出格式】

一个整数表示答案
"""
def dfs(x, y):
    if fig[x][y] == '.':
        return

    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for i in range(4):
        tx = x + direction[i][0]
        ty = y + direction[i][1]
        if 0 <= tx < n and 0 <= ty <= n and vis[tx][ty] != 1:
            if fig[tx][ty] == '.':
                fig[x][y] = '.'
                vis[x][y] = 1
                return


n = int(input())
fig = [list(input()) for _ in range(n)]
vis = [[0] * n for i in range(n)]
ans = 0

for i in range(n):
    for j in range(n):
        dfs(i, j)

for line in fig:
    for c in line:
        if c == '#':
            ans += 1

print(ans)