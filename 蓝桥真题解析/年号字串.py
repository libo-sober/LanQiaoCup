"""
小明用字母A 对应数字1，B 对应2，以此类推，用Z 对应26。对于27
以上的数字，小明用两位或更长位的字符串来对应，例如AA 对应27，AB 对
应28，AZ 对应52，LQ 对应329。
请问2019 对应的字符串是什么？
"""
# # 进制转换一般都是用除K取余法
# num = 2019
# print(num % 26, num // 26)
# print(77 % 26, 77 // 26)
# print(2 % 26, 2 // 26)
# print(chr(ord('A') + 17 - 1))
# print(chr(ord('A') + 25 - 1))
# print(chr(ord('A') + 2 - 1))
# # BYQ
# # 验算
# # LQ 329
# print(ord('Q')-ord('A')+1 + (ord('L')-ord('A')+1) * 26)  # 329
# # BYQ 2019
# print(ord('Q')-ord('A')+1 + (ord('Y')-ord('A')+1) * 26 + (ord('B')-ord('A')+1) * 26 ** 2)  # 2019
# # 所以提交BYQ
#
# # 2019 转成16进制
# # print(2019 % 16, 2019 // 16)
# # print(126 % 16, 126 // 16)
# # print(3 + 14 * 16 + 7 * 16 ** 2)
# # 7E3

# 最后整理一下代码
year = 2019
lst = []
while year != 0:
    lst.append(chr(ord('A') + year % 26 - 1))
    year = year // 26
# reversed(lst)
lst.reverse()
print(*lst)  # B Y Q
