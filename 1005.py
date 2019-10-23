'''
当我们验证卡拉兹猜想的时候，为了避免重复计算，可以记录下递推过程中遇到的每一个数。例如对 n=3 进行验证的时候，我们需要计算 3、5、8、4、2、1，则当我们对 n=5、8、4、2 进行验证的时候，就可以直接判定卡拉兹猜想的真伪，而不需要重复计算，因为这 4 个数已经在验证3的时候遇到过了，我们称 5、8、4、2 是被 3“覆盖”的数。我们称一个数列中的某个数 n 为“关键数”，如果 n 不能被数列中的其他数字所覆盖。现在给定一系列待验证的数字，我们只需要验证其中的几个关键数，就可以不必再重复验证余下的数字。你的任务就是找出这些关键数字，并按从大到小的顺序输出它们。
'''

numbers = []
n = int(input())
strnum = input().split()
for each in range(0, n):
    numbers.append(int(strnum[each]))
allsubs = []
for each in range(0, n):
    number = numbers[each]
    subs =[]
    while(number != 1):
        if number % 2 == 0:
            number = number // 2
        else:
            number = (number * 3 + 1) // 2
        subs.append(number)
    allsubs.append(subs)
removenum = []
for each in numbers:
    for i in allsubs:
        if each in i:
            removenum.append(each)
            break
for each in removenum:
    numbers.remove(each)
numbers = sorted(numbers, reverse=True)
print(numbers[0], end='')
for each in numbers[1:]:
    print(' ' + str(each), end='')

