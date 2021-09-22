'''
register注册类的测试类
'''
import unittest

from frame.study_unittest.register import register


class TestRegister(unittest.TestCase):

    def setUp(self) :
        print("{}---用例开始执行".format(self))

    def tearDown(self):
        print("{}---用例结束".format(self))

    def test_register_success(self):
        #测试 注册成功
        data = ('testname','password123','password123')  #测试数据，用户名 密码1 密码2
        expected ={'code':1,'msg':'注册成功'}  #预期结果
        result = register(*data)             #调用注册方法
        self.assertEqual(expected,result)     #断言

    def test_username_isnull(self):
        #测试 用户名为空
        data = ('', 'password123', 'password456')  # 测试数据，用户名 密码1 密码2
        expected = {'code': 0, 'msg': '所有参数不能为空'}  # 预期结果
        result = register(*data)  # 调用注册方法
        self.assertEqual(expected, result)  # 断言

    def test_username_lt6(self):
        #测试 用户名小于6位
        data = ('ttest', 'password123', 'password123')  # 测试数据，用户名 密码1 密码2
        expected = {'code': 0, 'msg': '用户名密码必须在6~18位之间'}  # 预期结果
        result = register(*data)  # 调用注册方法
        self.assertEqual(expected, result)  # 断言

    def test_pwd1_not_pwd2(self):
        #测试 用户名小于6位
        data = ('testtest', 'password123', 'password456')  # 测试数据，用户名 密码1 密码2
        expected = {'code': 0, 'msg': '两次密码输入不一致'}  # 预期结果
        result = register(*data)  # 调用注册方法
        self.assertEqual(expected, result)  # 断言

    @classmethod
    def setUpClass(cls) :
        print('-----class before-------')

    @classmethod
    def tearDownClass(cls):
        print('-----class after-------')

if __name__ == '__main__':
    unittest.main()        #需要调用unittest的main()来执行测试用例
