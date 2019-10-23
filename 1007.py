'''
让我们定义d(n)为：d(n)=p(n+1)-p(n),其中p(i)是第i个素数。显然有d(1)=1，且对于n>1有d(n)是偶数。“素数对猜想”认为“存在无穷多对相邻且差为2的素数”。现给定任意正整数N（<10^5)，请计算不超过N的满足猜想的素数对的个数。
'''

def prime(n, result):
    flag = [1] * (n + 2)
    p = 2
    while p <= n:
        result.append(p)
        for i in range(2 * p, n + 1, p):
            flag[i] = 0
        while 1:
            p += 1
            if flag[p] == 1:
                break


a = int(input())
result = []
prime(a, result)
num = 0
for i in range(len(result) - 1):
    if result[i + 1] - result[i] == 2:
        num += 1
print(num)


# 超时
# from math import sqrt
#
# pre = 2
# cnt = 0
# n = int(input())
# for i in range(3, n):
#     jj = 2
#     for j in range(2, int(sqrt(i)) + 1):
#         if i % j == 0:
#             break
#         jj += 1
#     if jj > sqrt(i):
#         if i - pre == 2:
#             cnt += 1
#         pre = i
# print(cnt)

