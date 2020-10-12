# 对一个数进行因式分解
# def factorization(num):
#     i = 2
#     while i ** 2 <= num:
#         while num % i == 0 and num != 1:
#             print(i, num / i)
#             num /= i
#         i += 1
#
#
# factorization(1001733993063167141)  # p = 891234941 q = 1123984201
p = 891234941
q = 1123984201
d = 212353
mod = (p - 1) * (q - 1)

for e in range(1000000000, 10000000000):
    if d * e % mod == 1:
        print(e)
        break




