#使用模块
#Python本身就内置了很多非常有用的模块，只要安装完毕，这些模块就可以立刻使用。
#我们以内建的sys模块为例，编写一个hello的模块：

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv
    if len(args)==1:
            print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()

def calc2(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
#第1行和第2行是标准注释，第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行，第2行注释表示.py文件本身使用标准UTF-8编码；
#第4行是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
#第6行使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名；
#以上就是Python模块的标准文件模板，当然也可以全部删掉不写，但是，按标准办事肯定没错。
#后面开始就是真正的代码部分。
#你可能注意到了，使用sys模块的第一步，就是导入该模块：
#import sys
#导入sys模块后，我们就有了变量sys指向该模块，利用sys这个变量，就可以访问sys模块的所有功能。
#sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称，例如：
#运行python3 hello.py获得的sys.argv就是['hello.py']；
#运行python3 hello.py Michael获得的sys.argv就是['hello.py', 'Michael]。
#最后，注意到这两行代码：
#if __name__=='__main__':
#    test()
#当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
#我们可以用命令行运行hello.py看看效果：
#$ python3 hello.py
#Hello, world!
#$ python hello.py Michael
#Hello, Michael!
#如果启动Python交互环境，再导入hello模块：
#$ python3
#Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 23 2015, 02:52:03) 
#[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
#Type "help", "copyright", "credits" or "license" for more information.
#>>> import hello
#>>>
#导入时，没有打印Hello, word!，因为没有执行test()函数。
#调用hello.test()时，才能打印出Hello, word!：
#>>> hello.test()
#Hello, world!

#作用域
#在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，有的函数和变量我们希望仅仅在模块内部使用。在Python中，是通过_前缀来实现的。
#正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等；
#类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量，hello模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名；
#类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；
#之所以我们说，private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，是因为Python并没有一种方法可以完全限制访问private函数或变量，但是，从编程习惯上不应该引用private函数或变量。
#private函数或变量不应该被别人引用，那它们有什么用呢？请看例子：
def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
#我们在模块里公开greeting()函数，而把内部逻辑用private函数隐藏起来了，这样，调用greeting()函数不用关心内部的private函数细节，这也是一种非常有用的代码封装和抽象的方法，即：
#外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。





#安装第三方模块
#在Python中，安装第三方模块，是通过包管理工具pip完成的。
#如果你正在使用Mac或Linux，安装pip本身这个步骤就可以跳过了。
#如果你正在使用Windows，请参考安装Python一节的内容，确保安装时勾选了pip和Add python.exe to Path。
#在命令提示符窗口下尝试运行pip，如果Windows提示未找到命令，可以重新运行安装程序添加pip。
#注意：Mac或Linux上有可能并存Python 3.x和Python 2.x，因此对应的pip命令是pip3。
#现在，让我们来安装一个第三方库——Python Imaging Library，这是Python下非常强大的处理图像的工具库。不过，PIL目前只支持到Python 2.7，并且有年头没有更新了，因此，基于PIL的Pillow项目开发非常活跃，并且支持最新的Python 3。
#一般来说，第三方库都会在Python官方的pypi.python.org网站注册，要安装一个第三方库，必须先知道该库的名称，可以在官网或者pypi上搜索，比如Pillow的名称叫Pillow，因此，安装Pillow的命令就是：
#pip install Pillow
#耐心等待下载并安装后，就可以使用Pillow了。
#有了Pillow，处理图片易如反掌。随便找个图片生成缩略图：
#>>> from PIL import Image
#>>> im = Image.open('test.png')
#>>> print(im.format, im.size, im.mode)
#PNG (400, 300) RGB
#>>> im.thumbnail((200, 100))
#>>> im.save('thumb.jpg', 'JPEG')
#其他常用的第三方库还有MySQL的驱动：mysql-connector-python，用于科学计算的NumPy库：numpy，用于生成文本的模板工具Jinja2，等等。

#模块搜索路径
#当我们试图加载一个模块时，Python会在指定的路径下搜索对应的.py文件，如果找不到，就会报错：
#>>> import mymodule
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#ImportError: No module named mymodule
#默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中：
#
#>>> import sys
#>>> sys.path
#['', '/Library/Frameworks/Python.framework/Versions/3.4/lib/python34.zip', '/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4', '/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/plat-darwin', '/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/lib-dynload', '/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/site-packages']
#如果我们要添加自己的搜索目录，有两种方法：
#一是直接修改sys.path，添加要搜索的目录：
#>>> import sys
#>>> sys.path.append('/Users/michael/my_py_scripts')
#这种方法是在运行时修改，运行结束后失效。
#第二种方法是设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。设置方式与设置Path环境变量类似。注意只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响。









