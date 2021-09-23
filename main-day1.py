import random
from math import sqrt


def xunhuan():
    """
    循环的示例代码偶数求和
    :return:
    """
    sum = 0
    for x in range(2, 101, 2):
        sum += x
    print(sum)

def xunhuan1():
    """
    循环1-100求和
    :return:
    """
    sum1=0
    for x1 in range(101):
        sum1 += x1
    print(sum1)

def jiujiu():
    """
    九九乘法表
    :return: 
    """
    for i in range(1, 10):
        for j in range(1, i+1):
            print('%d*%d=%d' % (i, j, i * j), end='\t')
            print()

def sushu():
    """
    素数判断
    :return:
    """
    num = int(input('请输入一个正整数: '))
    end = int(sqrt(num))
    is_prime = True
    for x in range(2, end + 1):
        if num % x == 0:
            is_prime = False
            break
    if is_prime and num != 1:
        print('%d是素数' % num)
    else:
        print('%d不是素数' % num)

def yueshu():
    """
    最大公约数和最小公倍数判断
    :return:
    """
    x = int(input('x = '))
    y = int(input('y = '))
# 如果x大于y就交换x和y的值
    if x > y:
        # 通过下面的操作将y的值赋给x, 将x的值赋给y
        x, y = y, x
# 从两个数中较的数开始做递减的循环
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
           print('%d和%d的最大公约数是%d' % (x, y, factor))
           print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
        break

def sanjiao():
    """
    打印三角形
    :return:
    """
row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()


for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()

if __name__ == '__main__':
    xunhuan()
    xunhuan1()
    jiujiu()
    sushu()
    yueshu()
    sanjiao()
    answer=random.randint(1,100)
    counter=0
    while True:
        counter += 1
        number = int(input('请输入一个数:'))
        if number<answer:
            print('大一点')
        elif number>answer:
            print('小一点')
        else:
            print('恭喜你，猜对了')
            break
        if counter > 7:
            print('你的智商明显余额不足，请充值')



