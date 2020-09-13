"""
标题： 购物单

小明刚刚找到工作，老板人很好，只是老板夫人很爱购物。
老板忙的时候经常让小明帮忙到商场代为购物。小明很厌烦，但又不好推辞。

这不，XX大促销又来了！老板夫人开出了长长的购物单，都是有打折优惠的。
小明也有个怪癖，不到万不得已，从不刷卡，直接现金搞定。
现在小明很心烦，请你帮他计算一下，需要从取款机上取多少现金，才能搞定这次购物。

取款机只能提供100元面额的纸币。小明想尽可能少取些现金，够用就行了。
你的任务是计算出，小明最少需要取多少现金。
以下是让人头疼的购物单，为了保护隐私，``物品名称被隐藏了。

****     180.90       88折
****      10.25       65折
****      56.14        9折
****     104.65        9折
****     100.30       88折
****     297.15       半价
****      26.75       65折
****     130.62       半价
****     240.28       58折
****     270.62        8折
****     115.87       88折
****     247.34       95折
****      73.21        9折
****     101.00       半价
****      79.54       半价
****     278.44        7折
****     199.26       半价
****      12.97        9折
****     166.30       78折
****     125.50       58折
****      84.98        9折
****     113.35       68折
****     166.57       半价
****      42.56        9折
****      81.90       95折
****     131.78        8折
****     255.89       78折
****     109.17        9折
****     146.69       68折
****     139.33       65折
****     141.16       78折
****     154.74        8折
****      59.42        8折
****      85.44       68折
****     293.70       88折
****     261.79       65折
****      11.30       88折
****     268.27       58折
****     128.29       88折
****     251.03        8折
****     208.39       75折
****     128.88       75折
****      62.06        9折
****     225.87       75折
****      12.89       75折
****      34.28       75折
****      62.16       58折
****     129.12       半价
****     218.37       半价
****     289.69       8折

需要说明的是，88折指的是按标价的88%计算，而8折是按80%计算，余者类推。
特别地，半价是按50%计算。

请提交小明要从取款机上提取的金额，单位是元。
答案是一个整数，类似4300的样子，结尾必然是00，不要填写任何多余的内容。

特别提醒：不许携带计算器入场，也不能打开手机。
"""
import math
from fnmatch import fnmatchcase as match
"""
这个求解方式很装逼，
但是，
蓝桥杯不允许导入第三方库，
又但是，
蓝桥杯是可以用python的标准库的，
math是python标准库可以用，fnmatch我上网查貌似也是python的标准库。
我不确定，有兴趣的小伙伴们可以取查一下。
所以大家知道导库解决更容易就行了。
实锤：
fnmatch.fnmatchcase(filename, pattern) 
Test whether filename matches pattern, returning True or False; 
the comparison is case-sensitive and does not apply os.path.normcase().
官方文档可查，fnmatch也是python标准库，蓝桥可以使用。
本题完全可以使用这种方法。
此外，
本方法也可以不加库，
把match(new_line[-1], '?折')改为new_line[-1]去掉'折'后判断剩余new_line[-1]字符串的长度，
为1则 time = int(new_line[-1][:-1]) * 0.1
为2则 time = int(new_line[-1][:-1]) * 0.01
普通应试解法参考链接：
https://blog.csdn.net/qq_31910669/article/details/103641497
在目录中选购物单即为本题目应试解法。
此方法需要用记事本先对数据进行格式化处理。
"""


def get_prices(file_name):
    prices = 0
    with open(file_name, mode='rt', encoding='utf-8') as f:
        info = f.readlines()
        for line in info:
            new_line = line.split()
            time = 0
            if new_line[-1] == '半价':
                time = 0.5
            elif match(new_line[-1], '?折'):
                time = int(new_line[-1][:-1]) * 0.1
            elif match(new_line[-1], '*折'):
                time = int(new_line[-1][:-1]) * 0.01
            prices += float(new_line[1]) * time

    return math.ceil(prices / 100) * 100


if __name__ == '__main__':
    print(get_prices('com_info'))  # 5200


"""
注释：
1. fnmatch模块
    fnmatch模块下的fnmatchcase方法
    fnmatchcase(匹配目标字符串, 需要匹配的通配符字符串)
    * 匹配多个
    ? 匹配一个
    可以匹配返回True
    否则返回False
2. math模块(math库蓝桥考试可以用，属于python的标准库)
    math模块下的ceil(x)方法：向上取整，x为500.45则返回501
    math模块下的floor(x)方法：向下取整，x为500.45则返回500
"""