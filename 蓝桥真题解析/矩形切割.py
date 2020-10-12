mat = [2019, 324]
# mat = [5, 3]
count = 0
while mat[0] >= 1 and mat[1] >= 1:
    mat[mat.index(max(mat))] = max(mat) - min(mat)
    count += 1
print(count)  # 21
