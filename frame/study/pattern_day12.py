'''
re模块用来支持正则表达式操作
compile(pattern, flags=0)
match(pattern, string, flags=0)

有很多人会选择[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)或[Lxml](http://lxml.de/)来进行匹配和信息的提取
'''
import re


# def  matchNameAndEmail ():
#     username = input('请输入名字:')
#     password = input('请输入密码:')
#
#     isname = re.match(r'^[0-9a-zA-Z_]{6,20}$',username)
#     ispwd = re.match(r'^[0-9]\d{6:20}$',password)
#
#     if not isname:
#         print('请输入正确的名称')
#     if not ispwd:
#         print('请输入正确的密码')
#     if isname and ispwd :
#         print('输入正确')
#
#
# if __name__ == '__main__':
#     matchNameAndEmail()

# def matchIphoneNum():
#     pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
#     sentence = '''
#     1重要的事情说13012345678遍，我的手机号是13512346789这个靓号，
#     不是15600998765，也是110或119，王大锤的手机号才是15600998765。
#     '''
#     iponeNumList = re.findall(pattern,sentence) #查询所有匹配的字符串，放到列表里
#     print(iponeNumList)
#     print()
#     iphoneIter = re.finditer(pattern,sentence)
#     for num in iphoneIter:
#         print(num) #<re.Match object; span=(32, 43), match='13512346789'>
#         print(num.group())   #13012345678
#
#     print()
#     iphoneNum = pattern.search(sentence)   #找到第一个就返回
#     print(iphoneNum.group())
#
#
# if __name__ == '__main__':
#     matchIphoneNum()
'''
屏蔽字符，sub():用指定的字符串替换原字符串中与正则表达式匹配的模式 可以用count指定替换的次数
'''
# def purify() :
#      sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
#      pattern = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔','*',sentence,flags=re.IGNORECASE)
#
#      print(pattern)
#
# if __name__ == '__main__':
#     purify()
'''
split(pattern, string, maxsplit=0, flags=0):用正则表达式指定的模式分隔符拆分字符串 返回列表
'''

def splitPoem():
    poem = '''
    海内存知己，天涯若比邻。
无为在歧路，儿女共占巾。
    '''
    sentence = re.split(r'[,.,.]',poem)
    print(sentence)

if __name__ == '__main__':
    splitPoem()

