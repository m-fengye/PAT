'''
给定一句英语，要求你编写程序，将句中所有单词的顺序颠倒输出。
测试输入包含一个测试用例，在一行内给出总长度不超过 80 的字符串。字符串由若干单词和若干空格组成，其中单词是由英文字母（大小写有区分）组成的字符串，单词之间用 1 个空格分开，输入保证句子末尾没有多余的空格。
'''
s1=input()
s1=s1.split()
s2=list(reversed(s1))
print(s2[0],end='')
for i in s2[1:]:
    print(' '+i,end='')
