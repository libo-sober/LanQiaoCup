"""
【问题描述】
小明对类似于 hello 这种单词非常感兴趣，这种单词可以正好分为四段，第一段由一个或多个辅音字母组成，第二段由一个或多个元音字母组成，第三段由一个或多个辅音字母组成，第四段由一个或多个元音字母组成。
给定一个单词，请判断这个单词是否也是这种单词，如果是请输出yes，否则请输出no。
元音字母包括 a, e, i, o, u，共五个，其他均为辅音字母。
【输入格式】
输入一行，包含一个单词，单词中只包含小写英文字母。
【输出格式】
输出答案，或者为yes，或者为no。
【样例输入】
lanqiao
【样例输出】
yes
【样例输入】
world
【样例输出】
no
【评测用例规模与约定】
对于所有评测用例，单词中的字母个数不超过100。
"""


def is_yuan(c):
    if c in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False


def yuan():
    global pos
    ans = 0
    while pos < len(s):
        if is_yuan(s[pos]):
            pos += 1
            ans += 1
        else:
            break
    return ans


def zhuo():
    global pos
    ans = 0
    # 0 为False 非0为True
    # 一共四段，如果哪段ans为0，则那段不符合规则
    while pos < len(s):
        if is_yuan(s[pos]):
            break
        pos += 1
        ans += 1
    return ans


def search():
    if zhuo() and yuan() and zhuo() and yuan() and pos == len(s):
        return True
    else:
        return False


pos = 0
s = input()

if search():
    print('yes')
else:
    print('no')


