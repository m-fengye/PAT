'''
1 字符串中必须仅有 P、 A、 T这三种字符，不可以包含其它字符；
2 任意形如 xPATx 的字符串都可以获得“答案正确”，其中 x 或者是空字符串，或者是仅由字母 A 组成的字符串；
3 如果 aPbTc 是正确的，那么 aPbATca 也是正确的，其中 a、 b、 c 均或者是空字符串，或者是仅由字母 A 组成的字符串。
数学归纳法 P左边的A个数*P和T之间A个数=T右边A的个数（P和T之间A个数>0 and 只包含P、A、T三种字符）
'''

def isYesNo(str):
    if str.count('P') + str.count('A') + str.count('T') == str.__len__():
        lena = str.find('P')
        lenb = str.find('T') - lena - 1
        lenc = str.__len__() - str.find('T') - 1
        if lenb != 0:
            if lena * lenb == lenc:
                return 1
    return 0


problem = []
num = int(input())
for each in range(0, num):
    problem.append(input())
for each in range(0, num):
    if isYesNo(problem[each]):
        print('YES')
    else:
        print('NO')

