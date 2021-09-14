'''
python的内置open函数，可以指定文件名、操作模式、编码信息等
操作模式：
r:读  w:写(会截断之前的内容) x:写(如果存在会产生异常)
a:追加 b:二进制模式  t:文本模式  +:更新
'''

# def open_file():
#     f = open('./test.txt','r',encoding='utf-8')
#     print(f.read())
#
#     f.close()
#
# if __name__ == '__main__':
#     open_file()

from math import sqrt

'''
异常：将可能出现状况的代码放在try代码块中，在try后面可以跟上多个except来捕获可能出现的异常状况
      finally块的代码无论程序正常或异常都会被执行，甚至调用sys模块的exit模块，finally块都会被执行
      with关键字制定文件对象的上下文环境并离开上下文环境时自动释放文件资源
'''
# def open_file():
#
#     try:
#        with open('./xx.txt','r',encoding='utf-8') as f:
#            print(f.read())
#     except FileNotFoundError as nofound:
#         print('File not found')
#     except LookupError:
#         print('未知编码')
#     except UnicodeDecodeError:
#         print('解码报错')
#     finally:
#         pass
#
# if __name__ == '__main__':
#     open_file()

'''
with关键字：上下文管理，适用于对资源进行访问的场合，确保不管使用过程中是否发生异常都会执行必要的'清理'操作，释放资源，
比如文件使用后自动关闭、线程中锁的自动获取和释放

工作原理:①with关键字后面的语句被执行后，返回对象的'__enter__()'方法
        ②这个方法的返回值会赋给as后面的遍历
        ③with的代码块全部执行完后，调用__exit__()方法
'''

'''
readline():读取一行
readlines():逐行读取,会将结果放到列表里
'''
# def open_file():
#     with open('./test.txt','r',encoding='utf-8') as f:
#         lines = f.readlines()
#         print(lines)
#
#
# if __name__ == '__main__':
#     open_file()

'''
w:写入文件
a：追加文件
'''
# def isprime(num):
#     assert num >= 1
#     for i in range(2,int(sqrt(num))+1):
#         if num % i == 0 :
#             return False
#         return True if num !=1 else  False
#
# def write_file():
#     files = ('a.txt','b.txt','c.txt')
#     txts = []
#     try:
#         for file in files :
#             txts.append(open(file,'w',encoding='utf-8'))
#
#         for num in range(1,10001):
#              if  isprime(num):
#                  if 1< num <= 100 :
#                      txts[0].write(str(num)+'\n')
#                  elif 100 < num <500:
#                      txts[1].write(str(num)+'\n' )
#                  else:
#                      txts[2].write(str(num)+'\n')
#     except IOError as ioerr:
#         print(ioerr)
#         print('io exception')
#     finally:
#         for f in txts:
#             f.close()
#
#     print('写完了')
#
# if __name__ == '__main__':
#     write_file()

'''
总结
1、写文件时，内容必须是str类型
2、关闭是必须要关file open的对象
3、用列表装入批量open的对象
4、二进制文件的读写不需要给encoding参数
'''
'''
读写二进制文件用wb 和rb
'''
# def open_jpg():
#     try:
#         with open('x.jpg','rb') as f1:
#             data = f1.read()
#             print(type(f1))
#
#         with open('y.jpg','wb') as f2:
#             f2.write(data)
#     except FileNotFoundError as err1:
#          print('file not found')
#     except IOError as err2:
#          print('io error')
#
#     print('end')
#
# if __name__ == '__main__':
#     open_jpg()
'''
json格式，JavaScript语言中创建对象的一种字面量语法
使用python的json模块可以将字典或列表以json格式进行保存
'''
import json
def parse_json():
    mydict = {
        'name': '骆昊',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('json.txt','w',encoding='utf-8') as f1:
            json.dump(mydict,f1)

    except FileNotFoundError as e1:
        print('file not found')
    except IOError as f2:
        print("io error")
    print('end')

if __name__ == '__main__':
    parse_json()

'''
json模块主要有四个比较重要的函数，分别是：

- `dump` - 将Python对象按照JSON格式序列化到文件中
- `dumps` - 将Python对象处理成JSON格式的字符串
- `load` - 将文件中的JSON数据反序列化成对象
- `loads` - 将字符串的内容反序列化成Python对象
'''



