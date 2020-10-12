import re
k = int(input())
s = input()
ans = 0
pattern = '\WAlice\W|\WBob\W' # 占了两个符位

while True:
    start = re.search(pattern, s).end()  # 第一个Alice 或 Bob的末尾索引
    name = re.search(pattern, s).group()
    name = re.search('\w+', name).group()  # 确定是Alice 还是 Bob
    s = s[start:]  # 检查过的第一部分丢掉，第二部分保留，因为下次还要用。
    if re.search(pattern, s):  # 能找到，找不到也就是没有Alice或者bob与前一个Alice或Bob匹配
        other = re.search(pattern, s).group()
        other = re.search('\w+', other).group() # 确定紧接着的是Alice 还是 Bob
        if name != other:  # 名字不同才进行
            end = re.search(pattern, s).start()  # 此时other对应的起始位置就是和上一个name直接的距离-2，因为模式有两个占位
        else:
            end = k + 1  # 名字相同不行 设置间距为比k大的数， 比如Bob love Bob ,我们要检测的是Bob ... Alice 或 Alice ... Bob
    else:
        # 如果剩下的s没有Alice或Bob则结束循环
        break
    if end + 2 <= k:  # pattern = '\WAlice\W|\WBob\W' # 占了两个符位
        ans += 1

print(ans)
"""
20
This is a story about Alice and Bob. Alice wants to send a private message to Bob. Bob love Alice.
3
"""