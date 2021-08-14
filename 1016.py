'''
正整数A的"DA(为1位整数)部分"定义为由A中所有DA组成的新整数PA。例如：给定A=3862767，DA=6，则A的"6部分"PA是66，因为A中有2个6。现给定A、DA、B、DB，请编写程序计算PA+PB。
'''
line=input().split(" ")
da=line[1]
db=line[3]

ca=0 if line[0].count(da)==0 else int(line[0].count(da)*da)
cb=0 if line[2].count(db)==0 else int(line[2].count(db)*db)
print(ca+cb)