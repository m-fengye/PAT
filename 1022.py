'''
输入两个非负10进制整数A和B(≤2**30−1)，输出A+B的D(1<D≤10)进制数。
'''
def fun1(num,n):
    str1 = ''
    if num == 0:
        return '0'
    while num != 0:
        str1 = str(num%n) + str1
        num//=n
    return str1


a,b,d = map(int,input().split(' '))
print(fun1(a+b,d))
