'''
if 语句，条件分支结构
用缩进表示代码的层次结构，建议不要使用制表键
'''

# username = input('请输入用户名:')
# password = input('请输入密码:')
# if username == 'admin' and password == '123456':
#     print('验证成功')
# else :
#     print('验证失败')

'''
if...elif...else语句，多重条件分支语句
'''
# x = float(input('x='))
# if x > 1 :
#     y = 3*x-5
# elif -1 <= x <= 1 :
#     y = x+2
# else :
#     y = 5*x+3
# print(f'(%.2f)=(%.2f)' %(x,y))

'''
练习1：英制单位英寸与公制单位厘米互换。
输入in、ch单位，长度，转换为另一单位长度
'''
# len = float(input('请输入长度:'))
# unit = input('请输入单位，ch 或 in：')
# if unit == 'ch':
#     print(f'%.2f厘米 -> %.2f英寸' % (len,len / 2.54))
# elif unit == 'in':
#     print(f'%.2f英寸 -> %.2f厘米' % (len, len * 2.54))   #注意，后面必须打括号
# else :
#     print("单位输入错误")

'''
练习2：#### 百分制成绩转换为等级制成绩。
要求：如果输入的成绩在90分以上（含90分）输出A；80分-90分（不含90分）输出B；
70分-80分（不含80分）输出C；60分-70分（不含70分）输出D；60分以下输出E。
'''
# score = int(input('请输入分数：'))
# if score >= 90:
#     print('A')
# elif 80 <= score < 90:
#     print('B')
# elif 70 <= score < 80:
#     print('C')
# elif 60 <= score < 70:
#     print('D')
# else :
#     print('E')

'''
练习3：判断输入的边长能否构成三角形，如果能则计算出三角形的周长和面积
'''
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
if a+b > c  and a+c > b and b+c > a :
    p = (a + b +c)/2
    area =  (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('周长:',p *2,'面积:',area)
else:
    print("不是三角形")

'''
总结：
1、 print(f'%.2f英寸 -> %.2f厘米' % (len, len * 2.54))   #注意，后面必须打括号
2、用变量代替常出现的数字
3、三角形的面积公式
'''