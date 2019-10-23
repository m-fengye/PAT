# 读入 n（>0）名学生的姓名、学号、成绩，分别输出成绩最高和成绩最低学生的姓名和学号。


class Student:
    def __int__(self):
        self.name = ''
        self.num = ''
        self.score = 0


n = int(input())
students = []
for each in range(0, n):
    stu = Student()
    info = input()
    stu.name = info[0: info.find(' ')]
    stu.num = info[info.find(' ') + 1:info.rfind(' ')]
    stu.score = int(info[info.rfind(' ') + 1:])
    students.append(stu)
maxStu = students[0]
minStu = students[0]
for each in range(1, n):
    if maxStu.score < students[each].score:
        maxStu = students[each]
    if minStu.score > students[each].score:
        minStu = students[each]
print(maxStu.name + ' ' + maxStu.num)
print(minStu.name + ' ' + minStu.num)
