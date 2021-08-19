'''
给定数字0-9各若干个。你可以以任意顺序排列这些数字，但必须全部使用。目标是使得最后得到的数尽可能小（注意0不能做首位）。例如：给定两个0，两个1，三个5，一个8，我们得到的最小的数就是10015558。
输入在一行中给出 10 个非负整数，顺序表示我们拥有数字 0、数字 1、……数字 9 的个数。整数间用一个空格分隔。10 个数字的总个数不超过 50，且至少拥有 1 个非 0 的数字。
在一行中输出能够组成的最小的数。
'''
num1 = list(map(int,input().split(' ')))
strNum = []
for i in range(10):
    for j in range(num1[i]):
        strNum.append(str(i))
strNum.sort()
for i in range(len(strNum)):
    if strNum[i] != '0':
        temp = strNum[0]
        strNum[0] = strNum[i]
        strNum[i] = temp
        break
print(''.join(strNum))