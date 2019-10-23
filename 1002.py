# 读入一个正整数 n，计算其各位数字之和，用汉语拼音写出和的每一位数字。

list1 = ['ling','yi','er','san','si','wu','liu','qi','ba','jiu']
def recursion(s):
    if s // 10 == 0:
        print(list1[s], end='')
        return
    else:
        recursion(s // 10)
        print(' ' + list1[s % 10], end='')


sum1 = 0
num = int(input())
while num > 0:
    sum1 += num % 10
    num //= 10
recursion(sum1)
