'''
请编写程序统计每种不同的个位数字出现的次数。例如：给定N=100311，则有2个0，3个1，和1个3。
'''
strNum = list(input())
count = [0]*10
for item in strNum:
    count[int(item)]+=1
for i in range(0,10):
    if count[i] != 0:
        print('{0}:{1}'.format(i,count[i]))