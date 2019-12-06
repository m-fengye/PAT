'''
大侦探福尔摩斯接到一张奇怪的字条：我们约会吧！ 3485djDkxh4hhGE 2984akDfkkkkggEdsb s&hgsfdk d&Hyscvnm。大侦探很快就明白了，字条上奇怪的乱码实际上就是约会的时间星期四 14:04，因为前面两字符串中第 1 对相同的大写英文字母（大小写有区分）是第 4 个字母 D，代表星期四；第 2 对相同的字符是 E ，那是第 5 个英文字母，代表一天里的第 14 个钟头（于是一天的 0 点到 23 点由数字 0 到 9、以及大写字母 A 到 N 表示）；后面两字符串第 1 对相同的英文字母 s 出现在第 4 个位置（从 0 开始计数）上，代表第 4 分钟。现给定两对字符串，请帮助福尔摩斯解码得到约会的时间。
'''
dicWeek = {'A':'MON','B':'TUE','C':'WED','D':'THU','E':'FRI','F':'SAT','G':'SUN'}
dicClock = {'0':'00','1':'01','2':'02','3':'03','4':'04','5':'05','6':'06','7':'07','8':'08','9':'09','A':'10','B':'11','C':'12','D':'13','E':'14','F':'15','G':'16','H':'17','I':'18','J':'19','K':'20','L':'21','M':'22','N':'23'}
str1 = []
for i in range(4):
    str1.append(input())
flag = 0
for i in range(len(str1[0])):
    if flag == 0:
        if str1[1].find(str1[0][i]) == i and 'A' <= str1[0][i] <= 'G':
            print(dicWeek[str1[0][i]],end=' ')
            flag = 1
    elif flag == 1:
        if str1[1].find(str1[0][i]) == i and ('0' <= str1[0][i] <= '9' or 'A' <= str1[0][i] <= 'N'):
            print(dicClock[str1[0][i]],end=':')
            flag = 2
            break
for i in range(len(str1[2])):
    if flag == 2:
        if str1[3].find(str1[2][i]) == i and ('a' <= str1[2][i] <= 'z' or 'A' <= str1[2][i] <= 'Z')):
            print('%02d' % i)
            break




string1=input()
string2=input()
string3=input()
string4=input()
Day={
"A":"MON","B":"TUE","C":"WED","D":"THU","E":"FRI","F":"SAT","G":"SUN"}
HH={"0":"00","1":"01","2":"02","3":"03","4":"04","5":"05","6":"06","7":"07","8":"08","9":"09","A":"10","B":"11","C":"12","D":"13","E":"14","F":"15","G":"16","H":"17","I":"18","J":"19","K":"20","L":"21","M":"22","N":"23"}
flag=0
for i in range(len(string1)):
        if string1[i]==string2[i] and string1[i].isupper() and('A'<=string1[i]<='G') and flag==0:
            day=string1[i]
            flag=1
        elif string1[i]==string2[i] and string1[i].isupper() and('A' <= string1[i] <= 'N') and flag==1:
            hh=string1[i]
            break
        elif string1[i]==string2[i] and string1[i].isdigit() and flag==1:
            hh=string1[i]
            break
for i in range(len(string3)):
        if string3[i]==string4[i] and string3[i].isalpha():
            mm=i
string=''
if 0<=mm<=9:
    mm=str(mm)
    mm='0'+mm
else:
    mm=str(mm)
string=Day.get(day,"nothing")+" "+HH.get(hh,"nothing")+":"+mm
print(string)

