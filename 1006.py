'''
让我们用字母 B 来表示“百”、字母 S 表示“十”，用 12...n 来表示不为零的个位数字 n（<10），换个格式来输出任一个不超过 3 位的正整数。例如 234 应该被输出为 BBSSS1234，因为它有 2 个“百”、3 个“十”、以及个位的 4。
'''

num = int(input())
string = ''
for i in range(1, num % 10 + 1):
    string += str(i)
num //= 10
for i in range(1, num % 10 + 1):
    string = 'S' + string
num //= 10
for i in range(1, num % 10 + 1):
    string = 'B' + string
print(string)

