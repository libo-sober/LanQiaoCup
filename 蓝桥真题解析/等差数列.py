"""
试题 H: 等差数列
时间限制: 1.0s 内存限制: 256.0MB 本题总分：20 分
【问题描述】
数学老师给小明出了一道等差数列求和的题目。但是粗心的小明忘记了一
部分的数列，只记得其中 N 个整数。
现在给出这 N 个整数，小明想知道包含这 N 个整数的最短的等差数列有
几项？
【输入格式】
输入的第一行包含一个整数 N。
第二行包含 N 个整数 A 1 ,A 2 ,··· ,A N 。(注意 A 1 ∼ A N 并不一定是按等差数
列中的顺序给出)
【输出格式】
输出一个整数表示答案。
【样例输入】

5
2 6 4 10 20
【样例输出】
10
【样例说明】
包含 2、6、4、10、20 的最短的等差数列是 2、4、6、8、10、12、14、16、
18、20。

【评测用例规模与约定】
对于所有评测用例，2 ≤ N ≤ 100000，0 ≤ A i ≤ 10^ 9 。
"""


def get_len():
    n = int(input())
    lst = list(map(int, input().split()))
    count = 1
    lst.sort()
    num = lst[0]
    dif = lst[1] - lst[0]
    for i in range(2, n):
        new_dif = lst[i] - lst[i - 1]
        dif = new_dif if new_dif < dif else dif
    while num < lst[-1]:
        num += dif
        count += 1
    return count


if __name__ == '__main__':
    print(get_len())

"""
注释：
1. sorted 排序
l1 = [22, 33, 1, 2, 7, 4]
l2 = sorted(l1)
# print(l1)  # [22, 33, 1, 2, 7, 4]  不会改变原来的数组内容
# print(l2)   # [1, 2, 4, 7, 22, 33]
l2 = [('太白',18), ('alex', 73), ('wusir', 35), ('口天吴', 41)]
print(sorted(l2))  # [('alex', 73), ('wusir', 35), ('口天吴', 41), ('太白', 18)]
print(sorted(l2, key=lambda x:x[1]))  # 返回的是一个列表  [('太白', 18), ('wusir', 35), ('口天吴', 41), ('alex', 73)]
print(sorted(l2, key=lambda x:x[1], reverse=True))  # 从大到小


2. 列表的sort()方法排序
l1.sort()
print(l1)  # [1, 2, 4, 7, 22, 33] 返回值为None 把原来的列表元素从小到大排序，改变原列表内容
l2 = [('太白',18), ('alex', 73), ('wusir', 35), ('口天吴', 41)]
l2.sort(key=lambda x: x[1])
# print(l2)  # [('太白', 18), ('wusir', 35), ('口天吴', 41), ('alex', 73)]
l2.sort(key=lambda x: x[1], reverse=True)
print(l2)  # [('alex', 73), ('口天吴', 41), ('wusir', 35), ('太白', 18)]  # 从大到小

"""