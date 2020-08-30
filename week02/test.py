# -*- coding:UTF-8 -*-
from operator import attrgetter
from collections import namedtuple
from operator import itemgetter
from operator import add
import functools


def func1():
    1/0
    print("func1 finally")
    print("after finally")


def func2(func3):
    try:
        print("func1 proformer")
        func3()
    except BaseException as e:
        # 这里能不或任何一层
        # 如果异常捕获程序流程会继续往下走，但是抛出的异常的地方堆栈会丢失
        print(e)
    finally:
        print("func2 finally")
    print("after finally")


class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value


st1 = Student()
st1.score = 100
print(st1.score)


# function parameters
# variable parameters
def cals(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(cals([1, 2, 3]))


def cals_vary(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(cals_vary(1, 2, 3))

# keywords parameters


def person(name, age, **kw):
    print('name', name, 'age', age, 'other', kw)


print(person('Michael', 30))

print(person('adam', 45, gender='M', job='Engineer'))

# *后的都是关键字变量


def f2(a, b, c, *, d, **f):
    print("a=", a, "b=", b, "c=", c, "d=", d, "f=", f)


print(f2(1, 2, 3, d=4, x={'m': 5, 'n': 6}))

# Decorator


def now():
    print("2015-3-25")


print(now.__name__)


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print("call %s:" % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now2():
    print("2015-3-25")


print(now2())

print(now2.__name__)


# def log_time(func):
#    def wrapper(*args, **kw):
#        print("call %s:", time.)


def metric(fn):
    # 首先是打印函数执行时间
    def print_exc_time(fn):
        def wrapper(*args, **kw):
            print(1111111111111111)
            r = fn(*args, **kw)
            print('%s executed in %s is' % (fn.__name__, 10.24))
            # 最终也是返回了r的执行结果。。。
            return r
        print("2222222222222222222")
        return wrapper
    return print_exc_time(fn)


@metric
def func_hello():
    print("0000000000000000000000")


######################################################################################################
# statictmethod classmethod 方法说明

class MyClass:
    def __init__(self, test):
        self.test = test

    def method(self):
        return 'instance method called', self

    # 这样创建的是一个单建
    @classmethod
    def classmethod(cls, text):
        cls.score = 100
        return cls(text)

    # 这样也是,指向的是一个地址
    @staticmethod
    def staticmethod(text):
        return MyClass(text)


obj2 = MyClass.staticmethod("123")
obj3 = MyClass.classmethod("345")
print(id(obj2))
print(id(obj3))
obj4 = MyClass.classmethod("678")


class Foo(object):
    def f(self): pass


class C(object):
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        print("set value", value)
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")

    __func__ = property(lambda self: print("hellworld"))


def factorial(n):
    '''returen n!'''
    return 1 if n < 2 else n * factorial(n-1)


print(factorial.__doc__)
print(dir(factorial))
print(type(factorial))
print(add(1, 2))

fruits = ['strawberry', 'fig', 'apple', 'cherry', "raspberry"]
print(sorted(fruits, key=lambda word: word[::-1]))


class TestHaha():
    __func__ = property(lambda self: print("hellworld"))


print(callable(classmethod))
print(callable(TestHaha()))
print(TestHaha().__func__)

metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

for city in sorted(metro_data, key=itemgetter(1)):
    print(city)

LatLong = namedtuple('LatLong', 'lat long')
Metropolis = namedtuple('Metropolis', 'name cc pop coord')

metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long))
               for name, cc, pop, (lat, long) in metro_data]


print(metro_areas[0])
print(metro_areas[0].coord.lat)
name_lat = attrgetter('name', 'coord.lat')
for city in sorted(metro_areas, key=attrgetter('coord.lat')):
    print(name_lat(city))


class testfunc(object):
    def func1():
        print("hello world")
        pass

    def __func__(self): return print("change world")


tt = testfunc()

print(dir(tt.func1))
print(tt.func1)
print(tt.func1.__func__)
tt.__func__()

def func1():
    print("change world")


def deco(func):
    def inner():
        print("running inner()")
        func()
    return inner

@deco
def target():
    print("running target")

print(target)