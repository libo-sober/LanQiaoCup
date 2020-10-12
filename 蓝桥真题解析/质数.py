def is_prim(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


ans = 0
i = 1
while i <= 2019:
    if is_prim(i):
        ans += 1
    i += 1

print(ans)  # 306
