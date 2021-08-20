'''
科学计数法是科学家用来表示很大或很小的数字的一种方便的方法，其满足正则表达式[+-][1-9].[0-9]+E[+-][0-9]+，即数字的整数部分只有1位，小数部分至少有1位，该数字及其指数部分的正负号即使对正数也必定明确给出。
现以科学计数法的格式给出实数A，请编写程序按普通数字表示法输出A，并保证所有有效位都被保留。
数字的存储长度不超过9999字节，且其指数的绝对值不超过9999。
'''
base,power = input().split('E')
out = '' if base[0] == '+' else '-'
base = base[1:2] + base[3:]
if power[0] == '+':
    if len(base) > int(power)+1:
        out += base[:int(power)+1]+'.'+base[int(power)+1:]
    else:
        out += base+'0'*(int(power)-len(base)+1)
else:
    out += '0.'+'0'*(-int(power)-1)+base
print(out)


# 测试点5  +5.0E+9 超出float范围
#a = input()
#flen = len(a[a.find('.')+1:a.find('E')])
#e = int(a[a.find('E')+1:])
#if e == 0:
#    print(a[1:a.find('E')])
#elif flen-e <= 0:
#    print(('{0:.0f}').format(float(a)))
#else:
#    print(('{0:.'+str(flen-e)+'f}').format(float(a)))