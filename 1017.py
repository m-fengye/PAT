'''
本题要求计算A/B，其中A是不超过1000位的正整数，B是1位正整数。你需要输出商数Q和余数R，使得A=B×Q+R成立。
'''
line=input().split(" ")
a=int(line[0])
b=int(line[1])
r=a//b
q=a%b
print('{0} {1}'.format(r,q))