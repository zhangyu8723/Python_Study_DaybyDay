'''
语言元素day2

1、input获取键盘输入的数字，且可以带字符串
2、取余符号% ，要用两个%%表示取余
3、%f表示浮点数，%d表示整数
'''

# a = int(input('a='))
# b = int(input('b='))
#
# print('%d + %d = %d ' % (a,b,a+b))
# print('%d - %d = %d ' % (a,b,a-b))
# print('%d * %d = %d ' % (a,b,a*b))
# print('%d / %d = %f ' % (a,b,a/b))
# print('%d %% %d = %d ' % (a,b,a%b))
# print('%d // %d = %d ' % (a,b,a//b))
# print('%d ** %d = %d' % (a,b,a**b))

'''
赋值运算符和复合赋值运算符
'''
# a = 10
# b = 3
# a += b     #a= a+b
# a *= a+2   #a= a *(a+2)
# print('a=',a)

'''
比较运算符和逻辑运算符
'''
# flag0 = 1==1
# flag1 = 3 >2
# flag2 = 2 < 1
# flag3 = flag1 and flag2
# flag4 = flag1 or flag2
# flag5 = not (1 != 2)
# print('flag0:', flag0)
# print('flag1:', flag1)
# print('flag2:', flag2)
# print('flag3:', flag3)
# print('flag4:', flag4)
# print('flag5:', flag5)

'''
练习1：将华式温度转换为摄氏温度
        转换公式$C=(F - 32) \div 1.8$。
'''
# fa = float(input('请输入华式温度：'))
# c = (fa - 32)/1.8
# print("%.1f华式温度 => %.1f摄氏温度" % (fa,c))
# print(f"{fa:.1f}华式温度 => {c:.2f}摄氏温度" )

'''
练习2：输入年份判断是不是闰年
'''
year = int(input('请输入年份:'))
isleap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(isleap)
