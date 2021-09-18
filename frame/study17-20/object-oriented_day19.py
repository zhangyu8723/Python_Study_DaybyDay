'''
面向对象三大支柱：封装、继承、多态
'''
import threading
from abc import ABCMeta, abstractmethod

'''
用工厂类创建对象
# '''
# class Employee(metaclass=ABCMeta):
#
#     def __init__(self,name):
#         self.name = name
#
#     @abstractmethod
#     def getSalary(self):
#         pass
#
# class Manager(Employee):
#
#     def getSalary(self):
#         return 20000.00
#
# class Programmer(Employee):
#     def __init__(self,name,workHour = 0):
#         super().__init__(name)
#         self.__workHour = workHour
#
#     def getSalary(self):
#         return self.__workHour *200
#
# class Salary(Employee):
#     def __init__(self, name, workHour=0):
#         super().__init__(name)
#         self.__workHour = workHour
#
#     def getSalary(self):
#         return 2000+self.__workHour *150
# #工厂类，实现对象使用者和对象之间的解耦
# class EmployeeCreate():
#     @staticmethod
#     def create(type,*args,**kwargs):
#         all_Employee = {'M': Manager, 'P': Programmer, 'S': Salary}
#         cls =all_Employee[type.upper()]
#         return  cls(*args,**kwargs) if cls else None
#
# def main():
#     emps = [
#         EmployeeCreate.create('M','Manager'),
#         EmployeeCreate.create('P','Programmer',120),
#         EmployeeCreate.create('S','Salary', 120)
#     ]
#
#
#     for emp in emps:
#         name = emp.name
#         salary = emp.getSalary()
#         print('name:%s ,salary:%.2f' % (name,salary))
#
# if __name__ == '__main__':
#     main()

'''
总结：1、通过工厂类实现创建类对象，通过类对象创建类实例，
2、通过类实例调用方法
'''

'''
魔方方法:
'''
'''
混入(mixin)
自定义字典限制只有在指定的key不存在时才能在字典中设置键值对
'''
# class SetOnceMappingMixin:
#     __slots__ = ()
#
#     def __setitem__(self, key, value):
#         if key in self:
#             raise KeyError(str(key) + ' already set')
#         return  super().__setitem__(key,value)
#
# class SetOnceDict(SetOnceMappingMixin,dict):  #自定义字典
#     pass
#
# my_dict = SetOnceDict()
# try:
#     my_dict['username'] = 'jack'
#     my_dict['username'] = 'mark'
# except KeyError as err:
#     print(err)
# print(my_dict)
'''
元编程和元类:象是通过类创建的，类是通过元类创建的，元类提供了创建类的元信息。所有的类都直接或间接的继承自`object`，所有的元类都直接或间接的继承自`type`。
'''
# class  SingletonMeta(type):
#     #自定义元类
#     def __init__(cls,*args,**kwargs):
#         cls.__instance = None
#         cls.__lock = threading.RLock()
#         super().__init__(*args,**kwargs)
#
#     def __call__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             with cls.__lock:
#                 if cls._instance is None:
#                     cls.__instance = super().__call__(*args,**kwargs)
#         return cls.__instance
#
# class President(metaclass=SingletonMeta):
#      pass
#

'''
- 面向对象设计原则

  - 单一职责原则 （**S**RP）- 一个类只做该做的事情（类的设计要高内聚）
  - 开闭原则 （**O**CP）- 软件实体应该对扩展开发对修改关闭
  - 依赖倒转原则（DIP）- 面向抽象编程（在弱类型语言中已经被弱化）
  - 里氏替换原则（**L**SP） - 任何时候可以用子类对象替换掉父类对象
  - 接口隔离原则（**I**SP）- 接口要小而专不要大而全（Python中没有接口的概念）
  - 合成聚合复用原则（CARP） - 优先使用强关联关系而不是继承关系复用代码
  - 最少知识原则（迪米特法则，Lo**D**）- 不要给没有必然联系的对象发消息

  > **说明**：上面加粗的字母放在一起称为面向对象的**SOLID**原则。

- GoF设计模式

  - 创建型模式：单例、工厂、建造者、原型
  - 结构型模式：适配器、门面（外观）、代理
  - 行为型模式：迭代器、观察者、状态、策略
'''
'''
可插拔的哈希算法(策略模式)
'''
class StreamHasher():
    def __init__(self , alg = 'md5',size = 4096):
        self.size = size
        alg = alg.lower()
        self.hasher = getattr(__import__('hashlib'),alg.lower())()

    def __call__(self, stream):
        return self.to_digest(stream)

    def to_digest(self,steam):
        #生成十六进制形式的摘要
        for buf in iter (lambda : steam.read(self.size), b''):
            self.hasher.update(buf)
        return self.hasher.hexdigest()

def main():
    hasher1 = StreamHasher()
    with open('Python-3.7.6.tgz','rb') as stream:
        print(hasher1.to_digest(stream))
    hasher2 = StreamHasher('sha1')
    with open('Python-3.7.6.tgz','rb') as stream:
        print(hasher2(stream))

if __name__ == '__main__':
    main()