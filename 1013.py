'''
令 P​i​​ 表示第 i 个素数。现任给两个正整数 M≤N≤10^​4​​，请输出 P​M​​ 到 P​N​​ 的所有素数。
'''
result = []#结果
flag = [0]*110000#标志
flag[0],flag[1],flag[2] = 1,1,0
count = 0#计数
li1 = [int(x) for x in input().split()]

for i in range(2,110000):
    if flag[i]==1:
        continue
    result.append(i)
    if len(result) >= 10000:
        break
    for j in range(2*i,110000,i):
        flag[j] = 1


result = result[li1[0]-1:li1[1]]
for i in range(0, len(result)):
    if i != 0 and i % 10 ==0:
        print()
    print(result[i], end='')
    if i % 10 != 9 and i != len(result) - 1:
        print(end=' ')
