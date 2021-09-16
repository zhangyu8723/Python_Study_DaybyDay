'''
for...in...循环,明确知道循环执行的次数时用for-in
- `range(101)`：可以用来产生0到100范围的整数，需要注意的是取不到101。
- `range(1, 101)`：可以用来产生1到100范围的整数，相当于前面是闭区间后面是开区间。
- `range(1, 101, 2)`：可以用来产生1到100的奇数，其中2是步长，即每次数值递增的值。
- `range(100, 0, -2)`：可以用来产生100到1的偶数，其中-2是步长，即每次数字递减的值。
'''
# sum = 0
# for x in range(0,10,2):
#     print("x=",x)
#     sum += x
#
# print('sum=',sum)
import random
from math import sqrt

'''
while循环,如果要构造不知道具体循环次数的循环结构，推荐使用`while`循环

猜数字游戏:计算机出一个1到100之间的随机数，玩家输入自己猜的数字，计算机给出对应的提示信息（大一点、小一点或猜对了），
如果玩家猜中了数字，计算机提示用户一共猜了多少次，游戏结束，否则游戏继续。
'''
#
# count = 0
# n = random.randint(1,101)
# while True :
#     count += 1
#     a = int(input('请输入数字:'))
#     if n > a :
#         print('小了')
#     elif n < a :
#         print('大了')
#     else:
#         print('猜对了')
#         break
# print('你一共猜了%d 次' % count)


'''
练习1：输入一个正整数判断是不是素数。
'''
# num = int(input('请输入一个数:'))
# end = int(sqrt(num))
# is_prime = False
# for x in range(2,end+1):
#     if num % x == 0 :
#         is_prime = True
#         break
#
# if is_prime and num != 1 :
#     print('%d 不是素数' % num)
# else :
#     print('%d 是素数' % num)

'''
练习2：输入两个正整数，计算它们的最大公约数和最小公倍数。
'''
# a = int(input("请输入数字:"))
# b = int(input('请输入数字:'))
# if a < b :
#     a , b = b ,a
# max_common_divisor = 0
# min_common_multiple = 0
# for x in range(b,0,-1):   #从后往前取
#     if b % x == 0 and a % x == 0 :
#         max_common_divisor = x
#         min_common_multiple = a * b //x
#         break
#
# print('%d ,%d的最大公约数是 %d' % (a,b,max_common_divisor))
# print('%d ,%d的最小公倍数是 %d' % (a,b,min_common_multiple))

'''
练习2：打印如下所示的三角形图案。
'''



