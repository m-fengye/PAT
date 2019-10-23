'''
卡拉兹(Callatz)猜想
对任何一个正整数 n，如果它是偶数，那么把它砍掉一半；如果它是奇数，那么把 (3n+1) 砍掉一半。这样一直反复砍下去，最后一定在某一步得到 n=1。我们今天的题目不是证明卡拉兹猜想，而是对给定的任一不超过 1000 的正整数 n，简单地数一下，需要多少步（砍几下）才能得到 n=1？
'''

sum1 = 0


def calltaz(n):
    global sum1
    if n == 1:
        return

    sum1 += 1
    if n % 2 == 0:
        calltaz(n / 2)
    else:
        calltaz((3 * n + 1) / 2)


num = int(input())
calltaz(num)
print(sum1)
