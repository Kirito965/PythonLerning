from random import randint

import main


def shuixian():
    """
    寻找100到1000的水仙花数
    :return:
    """
    for num in range(100, 1000):
        low = num % 10
        mid = num // 10 % 10
        high = num // 100
        if num == low ** 3 + mid ** 3 + high ** 3:
            print(num)

def fanzhuan():
    """
    整数翻转 12345变为54321
    :return:
    """
    num = int(input('num = '))
    reversed_num = 0
    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num //= 10
    print(reversed_num)


def ji():
    """
    百鸡百钱问题
    :return:
    """
    for x in range(0, 20):
        for y in range(0, 33):
            z = 100 - x - y
            if 5 * x + 3 * y + z / 3 == 100:
                print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))

def fiber():
    """
    斐波那契数列
    :return:
    """
    num = int(input('请输入要查看的斐波那契数列号：'))
    f1=1
    f2=1
    for i in range(1, num+1):
       if i==1:
           print('1    ')
       elif i==2:
           print('1    ')
       else:
        sum = f1+f2;
        f1 = f2
        f2 = sum
        print('%d' %(sum) ,end='\t')
        print()

def dubo():
    """
    赌博游戏
    :return:
    """
    money = 1000
    while money > 0:
        print('你的总资产为:', money)
        needs_go_on = False
        while True:
            debt = int(input('请下注: '))
            if 0 < debt <= money:
                break
        first = randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % first)
        if first == 7 or first == 11:
            print('玩家胜!')
            money += debt
        elif first == 2 or first == 3 or first == 12:
            print('庄家胜!')
            money -= debt
        else:
            needs_go_on = True
        while needs_go_on:
            needs_go_on = False
            current = randint(1, 6) + randint(1, 6)
            print('玩家摇出了%d点' % current)
            if current == 7:
                print('庄家胜')
                money -= debt
            elif current == first:
                print('玩家胜')
                money += debt
            else:
                needs_go_on = True
    print('你破产了, 游戏结束!')


if __name__ == '__main__':
    # shuixian()
    # fanzhuan()
    # ji()
    # fiber()
    # dubo()
    a=100
