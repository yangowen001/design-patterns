#  author: Michael
#  email: yangowen@126.com
# Note: 利用元类实现单例模式
class MyTpye(type):
    def __init__(cls, name, bases, attrs):
        cls.instance = None
        super().__init__(name, bases, attrs)

    def __new__(mcs, *args, **kwargs):
        new_cls = super().__new__(mcs, *args, **kwargs)
        return new_cls

    def __call__(cls, *args, **kwargs):
        if not cls.instance:
            instance = super().__call__(*args, **kwargs)
            cls.instance = instance
        return cls.instance


class Singleton(object, metaclass=MyTpye):
    pass


class Foo(Singleton):
    def __init__(self, name):
        self.name = name


f1 = Foo('xiao')
f2 = Foo('hua')
print(Foo.instance)
print(f1, f1.name)
print(f2, f2.name)
