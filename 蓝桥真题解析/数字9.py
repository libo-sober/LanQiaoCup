"""
【问题描述】
在1至2019中，有多少个数的数位中包含数字9？
注意，有的数中的数位中包含多个9，这个数只算一次。例如，1999这个数包含数字9，在计算只是算一个数。
【答案提交】
这是一道结果填空的题，你只需要算出结果后提交即可。本题的结果为一个整数，在提交答案时只填写这个整数，填写多余的内容将无法得分。
"""
def contain(num):
    while num != 0:
        temp = num % 10
        num = num // 10
        if temp == 9:
            return True
    return False


count = 0
for i in range(1, 2020):
    if contain(i):
        count += 1
print(count)
