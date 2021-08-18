'''
现给定所有种类月饼的库存量、总售价、以及市场的最大需求量，请你计算可以获得的最大收益是多少。
注意：销售时允许取出一部分库存。样例给出的情形是这样的：假如我们有3种月饼，其库存量分别为18、15、10万吨，总售价分别为75、72、45亿元。如果市场的最大需求量只有20万吨，那么我们最大收益策略应该是卖出全部15万吨第2种月饼、以及5万吨第3种月饼，获得72+45/2=94.5（亿元）。
每个测试用例先给出一个不超过1000的正整数N表示月饼的种类数、以及不超过500（以万吨为单位）的正整数D表示市场最大需求量。随后一行给出N个正数表示每种月饼的库存量（以万吨为单位）；最后一行给出N个正数表示每种月饼的总售价（以亿元为单位）。数字间以空格分隔。
对每组测试用例，在一行中输出最大收益，以亿元为单位并精确到小数点后2位。
'''
moonCakeType,marketDemand = map(int,input().split(' '))
stock = list(map(float,input().split(' ')))
totalPrice = list(map(float,input().split(' ')))
price = [a/b for a,b in zip(totalPrice,stock)]

list1 = [{'stock':a,'price':b,'totalPrice':c} for a,b,c in zip(stock,price,totalPrice)]
list1 = sorted(list1,key=lambda x:x['price'],reverse=True)

income = 0
num = 0
for item in list1:
    num=num+item['stock']
    if num > marketDemand:
        income+=item['totalPrice']*(item['stock']-num+marketDemand)/item['stock']
        break
    income+=item['totalPrice']

print('{0:.2f}'.format(income))