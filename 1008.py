'''
一个数组A中存有N（>0）个整数，在不允许使用另外数组的前提下，将每个整数循环向右移M（≥0）个位置，即将A中的数据由（A​0​​A​1​​⋯A​N−1​​）变换为（A​N−M​​⋯A​N−1​​A​0​​A​1​​⋯A​N−M−1​​）（最后M个数循环移至最前面的M个位置）。如果需要考虑程序移动数据的次数尽量少，要如何设计移动的方法？
'''
row_1 = input()
row_2 = input()
num = row_1.split(' ')
number = row_2.split(' ')
for i in range(0, 2):
    num[i] = int(num[i])
for i in range(len(number)):
    number[i] = int(number[i])
num[1] = (num[0] - num[1] % num[0]) % num[0]
print(number[num[1]], end='')
for i in number[num[1] + 1:]:
    print(' ' + str(i), end='')
for i in number[0:num[1]]:
    print(' ' + str(i), end='')
