'''
高阶函数:filter、map
'''
#filter过滤函数
# items1 = list(map(lambda x :x**2,filter ( lambda x : x%2 ,range(1,10))))
# print(items1)
# items2 = [x**2 for x in range(1,10) if x %2]
# print(items2)
from threading import RLock

'''
global:声明或定义全局变量，
nonlocal:声明使用嵌套作用域的遍历
'''

'''
装饰器函数
例子：输出函数执行时间的装饰器
'''
from functools import wraps
from time import time
#
# def record_time(func):
#     @wraps(func)
#     def wrapper(*args ,**kwargs):
#         start = time()
#         result = func(*args,**kwargs)
#         print(f'{func.__name__}:{time() - start} 秒')
#         return result
#     return wrapper()
'''
可以参数化的装饰器
'''
# def record(output):
#     def decorate(func):
#         @wraps(func)
#         def wrapper(*args,**kwargs):
#             start = time()
#             result = func(*args,**kwargs)
#             output(func.__name__,time() - start)
#             return result
#
#         return wrapper
#
#     return decorate

'''
定义类的方式定义装饰器
'''
# class Record():
#     def __init__(self,output):
#         self.output = output
#
#     def __call__(self, func):
#         @wraps(func)
#         def wrapper(*args,**kwargs):
#             start = time()
#             result = func(*args,**kwargs)
#             self.output(func.__name__,time() - start)
#             return result
#
#         return wrapper
#
'''
用装饰器来实现单例
'''
def singleton(cls):
    instances = {}
    locker = RLock()

    @wraps(cls)
    def wrapper(*args,**kwargs):
        if cls not in instances:
            with locker:           #加锁
                if cls not in instances:
                   instances[cls] = cls(*args,**kwargs)
        return instances[cls]
    return  wrapper

@singleton
class President:
    pass
