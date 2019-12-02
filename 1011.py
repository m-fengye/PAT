'''
给定区间 [−2​^31​​,2^​31​​] 内的 3 个整数 A、B 和 C，请判断 A+B 是否大于 C。
'''
strRows =[]
for i in range(0, int(input())):
    strRows.append(input())
for i in range(0, strRows.__len__()):
    e = [int(x) for x in strRows[i].split()]
    if int(e[0])+int(e[1]) > int(e[2]):
        print('Case #%d: true' % (i+1))
    else:
        print('Case #%d: false' % (i+1))
