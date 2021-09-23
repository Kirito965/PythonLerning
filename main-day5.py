import sys

"""
f=[x for x in range(1,10)]
print(f)
f=[x+y for x in 'ABCDE' for y in '1234567']
print(f)
f=[x**2 for x in range(1,1000)]
print(sys.getsizeof(f))
print(f)
for val in f:
    print(val)
"""

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    for val in fib(20):
        print(val)




if __name__ == '__main__':
    main()
    """
    元组的定义以及转换列表 tuple和list
    t = ('罗浩',38,True,'四川成都')
    print(t)
    print(t[0])
    print(t[3])
    for member in t:
        print(member)
    t=('王大锤',20,True,'云南昆明')
    print(t)
    person=list(t)
    print(person)
    person[0]='李小龙'
    person[1]=25
    print(person)
    fruit_list=tuple(person)
    print(fruit_list)
    """

    """
    集合
    set1={1,2,2,3,3,2}
    print(set1)
    print('Length=' ,len(set1))
    set2=set(range(1,10))
    print(set2)
    set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
    print(set4)
    """

    