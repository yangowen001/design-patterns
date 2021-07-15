#  author: Michael
#  email: yangowen@126.com


# 0. 接口
# 定义: 若干抽象方法(abstract method)的集合
# 作用: 限制实现接口的类必须按照接口给定的调用方式实现这些方法, 对高层模块隐藏了类的内部实现


# 1. 不使用接口, 定义两个支付类, 他们都有支付方法 供使用者调用
# Note: 接口要保证所调用方法的接口参数个数统一, 使用者无需针对每种对象写不同的调用函数
'''
但是, 这种方式没有任何约束, pay方法自由定义, 可以传入任意长的参数, 无法统一
'''


class AliPay:
    def pay(self, money):
        pass


class WeChatPay:
    def pay(self, money):
        pass


p = AliPay()
p.pay(100)

# 2. 定义一个基类, 约束pay方法的使用
'''
虽然规定了子类必须实现一个叫做pay的方法, 否则调用pay抛出异常:
    缺点: 不调用Pay方法不会报错
'''


class Payment:
    def pay(self, money):
        raise NotImplementedError


class AliPay(Payment):
    def pay(self, money):
        pass


class WeChat(Payment):
    def pay(self, money, *args):
        pass


# 3. 通过抽象基类来约束子类的方法
'''
本质: 
    1. 抽象类无法被实例化(否则报错), 所以子类如AliPay必须自己实现非抽象的pay方法
    2. 所有抽象方法必须被子类实现
'''

from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        # Note: 该方法无需实现, 但通常需要写好注释文档, 描述接口如何使用
        pass


class AliPay(Payment):
    def pay(self, money, *args):
        print(f'支付宝支付1元{args}')


class WeChatPay(Payment):
    def pay(self, money, *args):
        print('微信支付2元')

p = AliPay()