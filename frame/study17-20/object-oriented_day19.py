'''
面向对象三大支柱：封装、继承、多态
'''
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
