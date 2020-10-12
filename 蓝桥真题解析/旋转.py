n, m = list(map(int, input().split()))
fig = [list(map(int, input().split())) for i in range(n)]
new_fig = [[0 for i in range(n)] for i in range(m)]

for i in range(m):
    for j in range(n):
        new_fig[i][j] = fig[n-j-1][i]

for i in range(m):
    print(*new_fig[i])
"""
3 4
1 3 5 7
9 8 7 6
3 5 9 7
"""
