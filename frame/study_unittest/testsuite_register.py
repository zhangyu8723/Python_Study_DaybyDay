'''
用TestSuite测试套件来表示测试用例集

'''
import unittest
from frame.study_unittest import test_register
import HTMLTestRunner

suite = unittest.TestSuite()

#方法一：添加单条用例
case = test_register.TestRegister('test_register_success')#创建用例对象，通过用例类去创建测试用例对象，需要传入用例方法名
suite.addTest(case)   #添加用例导测试套件中

#方法二：添加多条用例,用列表的形式
case1 = test_register.TestRegister('test_username_isnull')
case2 = test_register.TestRegister('test_register_success')
suite.addTests([case1,case2])


#方法三：添加整个测试用例类
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(test_register.TestRegister))


#方法四:添加整个模块
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(test_register))


#方法五：指定测试用例所在的目录路径
#其中方式5，还可以自定义匹配规则，默认是会寻找目录下test*.py文件，即所有以test开头命名的py文件，自定义如下：
loader = unittest.TestLoader()
suite.addTest(loader.discover(r'd:\learn\python'))
