'''
给定一系列正整数，请按要求对数字进行分类，并输出以下 5 个数字：
    A​1​​ = 能被 5 整除的数字中所有偶数的和；
    A​2​​ = 将被 5 除后余 1 的数字按给出顺序进行交错求和，即计算 n​1​​−n​2​​+n​3​​−n​4​​⋯；
    A​3​​ = 被 5 除后余 2 的数字的个数；
    A​4​​ = 被 5 除后余 3 的数字的平均数，精确到小数点后 1 位；
    A​5​​ = 被 5 除后余 4 的数字中最大数字。

'''
num = map(int , input().split()[1:])
A1,A2,A3,A4,A5 = 0,0,0,0,0
j,p,k = 0,0,0
for i in num:
    if i%10 == 0:
        A1 += i
    if i%5 == 1:
        if j == 0 or j == 2:
            A2 += i
            j = 1
        else:
            A2 -= i
            j = 2
    if i%5 == 2:
        A3 += 1
    if i%5 == 3:
        p = p+1
        k += i
    if i%5 == 4:
        if i > A5:
            A5 = i
if k != 0:
    A4 = '%0.1f'%(k/p)
else:
    A4 = 0
if A1 == 0:
    print('N',end=' ')
else:
    print(A1,end=' ')
if A2 == 0 and j == 0:
    print('N',end=' ')
else:
    print(A2,end=' ')
if A3 == 0:
    print('N',end=' ')
else:
    print(A3,end=' ')
if A4 == 0:
    print('N',end=' ')
else:
    print(A4,end=' ')
if A5 == 0:
    print('N')
else:
    print(A5)
