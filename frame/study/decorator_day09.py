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

'''






