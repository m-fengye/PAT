'''
给定任一个各位数字不完全相同的4位正整数，如果我们先把4个数字按非递增排序，再按非递减排序，然后用第1个数字减第2个数字，将得到一个新的数字。一直重复这样做，我们很快会停在有“数字黑洞”之称的6174，这个神奇的数字也叫Kaprekar常数。
7766 - 6677 = 1089
9810 - 0189 = 9621
9621 - 1269 = 8352
8532 - 2358 = 6174
'''
def fun1(num):
    charNum = list('{0:0>4d}'.format(num))
    minNum = sorted(charNum)
    maxNum = sorted(charNum,reverse=True)
    minNum = int(''.join(minNum))
    maxNum = int(''.join(maxNum))
    return minNum,maxNum


num = int(input())
while True:
    minNum,maxNum = fun1(num)
    num = maxNum - minNum
    print('{0:0>4d} - {1:0>4d} = {2:0>4d}'.format(maxNum,minNum,num))
    if num == 6174 or num == 0:
        break