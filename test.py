#!/usr/bin/env python3
# -*- coding: utf-8 -*-





###输入输出
#name = input()
print('The quick brown fox', 'jumps over', 'the lazy dog')
#name = input('please enter your name:')
#print('hello ' + name)





###数据类型和变量
#如果字符串里面有很多字符都需要转义，就需要加很多\，为了简化，Python还允许用r''表示''内部的字符串默认不转义，可以自己试试：
print('\\\t\\')
print(r'\\\t\\')
print(r'Hello, "Bart"')

#如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容,多行字符串'''...'''还可以在前面加上r使用，请自行测试。
print('''line1
line2
line3''')
print(r'''line1
line2
line3''')

#还有一种除法是//，称为地板除，两个整数的除法仍然是整数：
print(10 // 3)

#在Python中，通常用全部大写的变量名表示常量：
PI = 3.14159265359
#但事实上PI仍然是一个变量，Python根本没有任何机制保证PI不会被改变，所以，用全部大写的变量名表示常量只是一个习惯上的用法，如果你一定要改变变量PI的值，也没人能拦住你。





###字符串和编码
#对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))






###使用list和tuple
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(classmates[2])
#如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：
print(classmates[-1])
#list是一个可变的有序表，所以，可以往list中追加元素到末尾：
classmates.append('Adam')
print(classmates)
#也可以把元素插入到指定的位置，比如索引号为1的位置：
classmates.insert(1, 'Jack')
print(classmates)
#要删除list末尾的元素，用pop()方法：
classmates.pop()
print(classmates)
#要删除指定位置的元素，用pop(i)方法，其中i是索引位置：
classmates.pop(1)
print(classmates)
#要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
classmates[1] = 'Sarah'
print(classmates)
#list里面的元素的数据类型也可以不同，比如：
L = ['Apple', 123, True]
print(L)
#t元素也可以是另一个list，比如：
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))
print(s)
#要注意s只有4个元素，其中s[2]又是一个list，如果拆开写就更容易理解了
p = ['asp', 'php']
s2 = ['python', 'java', p, 'scheme']
print(s)
print(s[2][-1])
#如果一个list中一个元素也没有，就是一个空的list，它的长度为0：
L2 = []
print(L2)
print(len(L2))

#另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：
classmatesT = ('Michael', 'Bob', 'Tracy')
print(classmatesT)
#现在，classmates这个tuple不能变了，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。
#不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。
#tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来，比如：
t = (1, 2)
#如果要定义一个空的tuple，可以写成()：
t = ()
#但是，要定义一个只有1个元素的tuple，如果你这么定义：
#t = (1)
#定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
#所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：
t = (1,)
print(t)
#最后来看一个“可变的”tuple：
#表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
t1 = ('a', 'b', ['A', 'B'])
t1[2][0] = 'X'
t1[2][1] = 'Y'
print(t1)





#条件判断和循环
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
#input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数。Python提供了int()函数来完成这件事情：
#s = input('birth: ')
#birth = int(s)
#if birth < 2000:
#    print('00前')
#else:
#    print('00后')

#Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来，看例子：
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
#如果要计算1-100的整数之和，从1写到100有点困难，幸好Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。
#range(101)就可以生成0-100的整数序列，计算如下：
sum = 0
for x in range(101):
    sum = sum + x
print(sum)
#第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。比如我们要计算100以内所有奇数之和，可以用while循环实现：
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)





#使用dict和set
#Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
#把数据放入dict的方法，除了初始化时指定外，还可以通过key放入：
d['Adam'] = 67
print(d['Adam'])
#如果key不存在，dict就会报错,要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
print('Thomas' in d)
#二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value：
print(d.get('Thomas'))
print(d.get('Thomas', -1))
#注意：返回None的时候Python的交互式命令行不显示结果。
#要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
d.pop('Bob')
print(d)
#请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。

#和list比较，dict有以下几个特点：
#查找和插入的速度极快，不会随着key的增加而变慢；
#需要占用大量的内存，内存浪费多。
#而list相反：
#查找和插入的时间随着元素的增加而增加；
#占用空间小，浪费内存很少。
#所以，dict是用空间来换取时间的一种方法。

#dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。
#这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。
#要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：

#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
#要创建一个set，需要提供一个list作为输入集合：
s = set([1, 2, 3])
print(s)
#注意，传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素，显示的顺序也不表示set是有序的。。
#重复元素在set中自动被过滤：
s = set([1, 1, 2, 2, 3, 3])
print(s)
#通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
s.add(4)
print(s)
s.add(4)
print(s)
#通过remove(key)方法可以删除元素：
s.remove(4)
print(s)
#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)
#set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。试试把list放入set，看看是否会报错。

#不可变对象
#str是不变对象，而list是可变对象。
#对于可变对象，比如list，对list进行操作，list内部的内容是会变化的，比如：
a = ['c', 'b', 'a']
a.sort()
print(a)
#而对于不可变对象，比如str，对str进行操作呢：
a1 = 'abc'
print(a1.replace('a', 'A'))
print(a1)
#所以，对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。
#tuple也是不可变对象
d = {(1,2,3): 95}
print(d)





#调用函数
#求绝对值函数
print(abs(100))
print(abs(-20))
#函数max()可以接收任意多个参数，并返回最大的那个：
print(max(1, 2))
print(max(2, 3, 1, -5))
#Python内置的常用函数还包括数据类型转换函数
print(int('123'))
print(int(12.34))
print(float('12.34'))
print(str(1.23))
print(str(100))
print(bool(1))
print(bool(''))
#函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
a = abs # 变量a指向abs函数
print(a(-1)) # 所以也可以通过a调用abs函数
#请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串
print(hex(100))





#定义函数
#在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。
#我们以自定义一个求绝对值的my_abs函数为例：
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-3))
#如果想定义一个什么事也不做的空函数，可以用pass语句：
def nop():
    pass
#pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
#pass还可以用在其他语句里，比如：
if age >= 18:
    pass
#缺少了pass，代码运行就会有语法错误。
#让我们修改一下my_abs的定义，对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现：
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
#print(my_abs('a'))
#函数可以返回多个值吗？答案是肯定的。
#比如在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的新的坐标：
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
#import math语句表示导入math包，并允许后续代码引用math包里的sin、cos等函数。
#然后，我们就可以同时获得返回值：
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
#但其实这只是一种假象，Python函数返回的仍然是单一值：
r = move(100, 100, 60, math.pi / 6)
print(r)
#原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。
#计算平方根可以调用math.sqrt()函数
print(math.sqrt(2))





#函数的参数
#默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(5))
print(power(5,3))
#设置默认参数时，有几点要注意：
#一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
#二是如何设置默认参数。
#当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
print(enroll('Sarah', 'F'))
#有多个默认参数时，调用的时候，既可以按顺序提供默认参数，比如调用enroll('Bob', 'M', 7)，意思是，除了name，gender这两个参数外，最后1个参数应用在参数age上，city参数由于没有提供，仍然使用默认值。
#也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上。比如调用enroll('Adam', 'M', city='Tianjin')，意思是，city参数用传进去的值，其他默认参数继续使用默认值。

#默认参数很有用，但使用不当，也会掉坑里。默认参数有个最大的坑，演示如下：
#先定义一个函数，传入一个list，添加一个END再返回：
def add_end(L=[]):
    L.append('END')
    return L
#当你正常调用时，结果似乎不错：
#>>> add_end([1, 2, 3])
#[1, 2, 3, 'END']
#>>> add_end(['x', 'y', 'z'])
#['x', 'y', 'z', 'END']
#当你使用默认参数调用时，一开始结果也是对的：
#>>> add_end()
#['END']
#但是，再次调用add_end()时，结果就不对了：
#>>> add_end()
#['END', 'END']
#>>> add_end()
#['END', 'END', 'END']
#很多初学者很疑惑，默认参数是[]，但是函数似乎每次都“记住了”上次添加了'END'后的list。
#原因解释如下：
#Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
#所以，定义默认参数要牢记一点：默认参数必须指向不变对象！
#要修改上面的例子，我们可以用None这个不变对象来实现：
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
#现在，无论调用多少次，都不会有问题：
#>>> add_end()
#['END']
#>>> add_end()
#['END']






