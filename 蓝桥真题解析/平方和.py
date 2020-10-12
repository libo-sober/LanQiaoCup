total = 0

for i in range(1, 2020):
    num = i
    while num != 0:
        a = num % 10
        if a in [2, 0, 1, 9]:
            total += i ** 2
            break
        num = num // 10

print(total)
# 2658417853
