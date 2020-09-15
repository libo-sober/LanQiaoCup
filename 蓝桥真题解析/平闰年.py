"""
问题描述

给定一个年份，判断这一年是不是闰年。

输入格式
输入包含一个整数y，表示当前的年份。
输出格式
输出一行，如果给定的年份是闰年，则输出yes，否则输出no。

说明：当试题指定你输出一个字符串作为结果（比如本题的yes或者no，你需要严格按照试题中给定的大小写，写错大小写将不得分。
样例输入
2013
样例输出
no
样例输入
2016
样例输出
yes
数据规模与约定
1990 <= y <= 2050。
"""
# 装逼解法
import datetime  # python的标准库，蓝桥考试可以放心使用

year = int(input())
# class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
# All arguments are optional and default to 0. Arguments may be integers or floats, and may be positive or negative.
time_delta = datetime.timedelta(days=1)  # 存储时间的变化量
# class datetime.date(year, month, day)
dt = datetime.date(year=year, month=3, day=1)  # 指定输入年份的3月1号

res = dt - time_delta  # 让dt存储的日期往前走一天
# print(dt)

if res.day == 29:  # 如果那年的2月分又29天为闰年
    print('yes')
else:
    print('no')

