'''
面向对象：把一组数据结构和处理它们的方法组成对象，把相同行为的对象归纳为类(class)，通过类的封装(encapsulation)隐藏内部细节
，通过继承(inheritance)实现类的特化(specialization)和泛化(feneralization)，通过多态(polymorphism)实现基于对象类型的动态分派
面向对象三大要素：封装、继承、多态
'''

# class Student (object) :
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def study(self, course_name):
#         print("%s正在学习%s" % (self.name,course_name))
#
#     def play(self,game_name):
#         if self.age >= 18:
#             print('%s正在玩%s' % (self.name,game_name))
#         else:
#             print('%s 年龄 %d，太小了，不能玩游戏' % (self.name , self.age))
#
# def main():
#     student1 = Student('AA',17)
#     student1.study('python')
#     student1.play('LOL')
#
# if __name__== '__main__':
#     main()
from time import sleep

'''
私有属性、方法: 以两个下划线开头的方法或属性， __method 
受保护方法:以一个下划线开头的方法或属性， _method
但是可以通过类名来访问私有属性、私有方法
'''
# class Student:
#     def __init__(self,name ,age):
#         self.name = name
#         self.age = age
#
#     def __sleep(self):
#         print("%s is sleeping" % self.name)
#
#
# def main():
#     student1 = Student('wa',19)
#     #student1.__sleep()  #只是用对象名.私有方法，会报错
#     print(student1.__dir__())
#
#     student1._Student__sleep()  #通过对象名.类名.私有方法()
#     #student1._Student.__sleep()  #错误示范
# if __name__ == '__main__':
#     main()

'''
练习1：定义一个类描述数字时钟
'''
class Clock :
    def __init__(self,hour,minute,second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def run(self):
        self.second += 1
        if self.second == 60 :
            self.minute += 1
            self.second = 0
            if self.minute == 60 :
                self.hour += 1
                self.minute = 0
                if self.hour == 24:
                    self.hour += 1

    def show(self):
        print('%02d:%02d:%02d' % (self.hour,self.minute,self.second))

def main():
    clock = Clock(23,17,5)
    while True :
        sleep(1)
        clock.run()
        clock.show()

if __name__ == '__main__':
    main()






