'''
@property装饰器：建议用单下划线开头，通过属性的getter(访问器)和setter(修改器)进行操作
1、对私有属性，设置get方法，并添加@property标签
2、对添加@property标签的方法，添加@属性名_setter标签
3、调用的时候通过类名.私有属性名， 会先调@property标签的get方法
4、设置私有属性值的时候，会调用@setter标签方法
'''
# class Person :
#     def __init__(self,name,age):
#         self._name = name
#         self._age = age
#
#     @property
#     def name(self):
#         return self._name
#
#     @property
#     def get_age(self):
#         return self._age
#
#     @name.setter
#     def name(self,name):
#         self._name = name
#
#     @get_age.setter
#     def set_age(self,age):
#         self._age = age
#
# def main():
#     person = Person('ki',18)
#     print('age=%d' % (person._age))
#     person.set_age=30
#     print('age=%d' % (person._age))
#     person.name='lalal'
#     print('name=%s' % (person._name))
#
#
# if __name__ == '__main__':
#     main()

from math import sqrt


'''
__slots__魔法方法:限定自定义对象只能绑定某些属性
'''
# class Person :
#     __slots__ = ('_name','_age')  #当只有_name一个属性时，运行报错，两个属性都添加时，运行正常
#
#     def __init__(self,name,age):
#         self._name = name
#         self._age = age
#
#     @property
#     def name(self):
#         return self._name
#
#     @property
#     def age(self):
#         return self._age
#
#     @name.setter
#     def name(self,name):
#        self._name = name
#
#     @age.setter
#     def age(self,age):
#         self._age = age
#
#
# def main():
#     person = Person('cc',80)
#     person.name = 'aa'
#     print('name= %s',person.name)
#
#
# if __name__ == '__main__':
#     main()

'''
静态方法：属于类的方法 ，在方法上面加上@staticmethod标签
'''
# class Triggle :
#
#     def __init__(self,a,b,c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     @staticmethod
#     def isTriggle(a,b,c):  #判断是否能构成三角形
#         return  a + b > c and b + c > a and a + c > b
#
#     def perimeter(self):
#         return self.a+ self.b+ self.c
#
#     def area(self):
#         half = self.perimeter() / 2
#         return sqrt(half * (half - self.a) *
#                     (half - self.b) * (half - self.c))
#
#
# def main():
#     if Triggle.isTriggle(3,4,5):
#        triggle = Triggle(3,4,5)
#        # print('周长:%d ' % triggle.perimeter())
#        # print('面积:%.2f ' % triggle.area())
#
#        print('周长: %d' % Triggle.perimeter(triggle))  #通过类调用成员方法时，要将对象作为参数传入
#        print('面积: %.2f' % Triggle.area(triggle))  # 通过类调用成员方法时，要将对象作为参数传入
#
#     else:
#         print('这不是三角形')
#
# if __name__ == '__main__':
#     main()
'''
类方法:代表当前类相关的信息的对象，第一个参数名约定为cls。类本身也是一个对象或者称之为元数据对象，
通过这个cls参数我们可以获取和类相关的信息，并且创建出类的对象
'''
# from time import localtime, time, sleep
# class Clock :
#     def __init__(self,hour = 0,minute = 0,second = 0):
#        self.hour = hour
#        self.minute = minute
#        self.second = second
#
#     @classmethod
#     def set_now(cls):
#         ctime = localtime(time())
#         return cls(ctime.tm_hour,ctime.tm_min,ctime.tm_sec)   #类方法，把当前时间设置进去
#
#     def show(self):
#         print('%02d:%02d:%02d' % (self.hour,self.minute,self.second))
#
#     def run(self):
#         self.second += 1
#         if self.second == 60:
#             self.minute += 1
#             if self.minute == 60:
#                 self.hour += 1
#                 if  self.hour == 24:
#                     self.hour = 0
#
# def main():
#     clock = Clock.set_now()
#     while True :
#         clock.show();
#         sleep(1)
#         clock.run()
#
# if __name__ == '__main__':
#     main()
#
'''
 总结:1、小数的打印方式 %02f ，默认是6位小数
      2、整数的打印方式 %02d, 两位数字占位，不足的话，前面补0
'''
'''
类之间的关系:
1、继承或泛化(is-a)：在类名后面加上(父类)
2、关联关系(has-a): 部门和员工、汽车和零件
3、依赖关系(use-a): 某个方法的参数中使用到了a
'''
# class Person:
#     def __init__(self,name,age):
#         self._name = name
#         self._age = age
#
#     @property
#     def name(self):
#         return self._name
#
#     @property
#     def age(self):
#         return self._age
#
#     @name.setter
#     def name(self,name):
#         self._name = name
#
#     @age.setter
#     def age(self,age):
#         self._age = age
#
#     def play(self,game):
#         print('%s 正在玩 %s ' % (self._name , game))
#
# class Student(Person): #继承person类
#
#     def __init__(self, name, age, course):
#         self._name = name
#         self._age = age
#         self._course = course
#
#     @property
#     def course(self):
#         return self._course
#
#     @course.setter
#     def course(self,course):
#         self._course = course
#
#     def play(self,game):
#         print('年龄为%d 的孩子不能玩%s,只能学习%s' % (self._age,game,self._course))
#
# def main():
#     student = Student('小a',15,'math')
#     student.play('农药')
#     person = Person('老c',32)
#     person.play('农药')
#
# if __name__ == '__main__':
#     main()
'''
抽象类:不能创建对象的类，可以通过abc模块的ABCMeta元类和abstractmethod包装器来达到抽象类的效果
'''
from abc import ABCMeta, abstractmethod


class Pet(metaclass = ABCMeta):

    def __init__(self, name):
        self._name = name

    @abstractmethod
    def make_voice(self, voice):
        pass
        print('%s的叫声是%s' % (self._name,voice))

class Dog(Pet):
    def __init__(self, name):
        self._name = name

    def make_voice(self, voice):
        print('%s的叫声是 %s  ~~~' % (self._name, voice))

class Cat(Pet):
    def __init__(self, name):
        self._name = name

    def make_voice(self, voice):
        print('%s的叫声是 %s  ！！' % (self._name, voice))

def main():

    dog = Dog('小汪')
    dog.make_voice('汪汪汪')
    cat = Cat('小猫')
    cat.make_voice('喵喵喵')



if __name__ == '__main__':
    main()


