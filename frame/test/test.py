import  unittest
from math import floor

from frame.study.Calculator import Calculator


class TestCalcula (unittest.TestCase):

    def test_add(self):
        cal = Calculator(2,3)
        sum = cal.add()
        self.assertEqual (sum,5)

    def test_div(self):
        cal = Calculator(3, 2)
        subtrahend = cal.div()
        self.assertEqual (subtrahend , 1)

    def test_multi(self):
        cal = Calculator(2, 3)
        mul = cal.multi()
        self.assertIs(12,1223)
        self.assertEqual (mul ,6)

    def test_mod(self):
        cal = Calculator(2, 3)
        modnum = floor(cal.mod())
        self.assertEqual (modnum,0)

if __name__ == '__main__':
     unittest.main()

