def hanoi(number, x, y, z):
    if number < 1:
        print('请输入一个正整数！')
        return -1
    if number == 1:
        print(x, '-->', z)  # 将x上的盘子移动到z上
    else:
        hanoi(number - 1, x, z, y)  # 将前n-1个盘子从x移动到y上
        print(x, '-->', z)  # 将最底下的盘子从x移动到z上
        hanoi(number - 1, y, x, z)  # 将y上的n-1个盘子移动到z上


n = int(input('请输入汉诺塔层数:'))
hanoi(n, 'X', 'Y', 'Z')
