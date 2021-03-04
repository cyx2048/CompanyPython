"""
定义至少有两个方法的类：
get string：从控制台输入获取字符串
print string：以大写形式打印字符串。
也请包含简单的测试函数来测试类方法。
"""

"""方法1"""
class test1():
    def input(self):                         #类方法里面必须有self参数
        self.i=input("input the string:")
    def up(self):
        self.j=self.i.upper()
    def out(self):
        print(self.j)
x=test1()
x.input()
x.up()
x.out()

"""方法2"""
class test2():
    def __init__(self):              #这里使用构造函数，该方法在类实例化时会自动调用
        self.s=""
    def getstring(self):
        self.s=input("input the string2:")
        self.l=self.s.upper()
    def outstring(self):
        print(self.l)

y=test2()
y.getstring()
y.outstring()
