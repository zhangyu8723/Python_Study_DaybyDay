'''

requests是一个基于HTTP协议来使用网络的第三库，其[官方网站](http://cn.python-requests.org/zh_CN/latest/)
有这样的一句介绍它的话：“Requests是唯一的一个**非转基因**的Python HTTP库，人类可以安全享用
'''
# import requests
#
# def main():
#     resp = requests.get('url')
#     data_json = resp.json()
#     for data in data_json:
#         url = data['url']
#
# if __name__ == '__main__':
#     main()


'''
套接字:一套用C语言写成的应用程序开发库，主要用于实现进程间同学和网络编程，
python的套接字有：流套接字(TCP套接字)、数据报套接字和原始套接字、

TCP套接字：使用TCP协议提供的传输服务来实现网络通讯的编程接口，在python中可以通过创建socket对象并指定type属性为sock_stream来使用TCP套接字

'''
# from socket import socket, AF_INET, SOCK_STREAM
# from datetime import datetime
#
# def main():
#     '''
#     1、创建套接字对象并指定使用哪种传输服务
#        family = AF_INET  --ipv4地址
#        family = AF_INET6 --IPV6地址
#        type = sock_stream  TCP套接字
#        type = sock_dgram  UDP套接字
#        type = sock_ram  原始套接字
#        server = socket(family = AF_INET,type = SOCK_STREAM)
#        '''
#     server = socket(family = AF_INET,type = SOCK_STREAM)
#
#     #2.绑定IP地址和端口，同一时间在同一端口上只能绑定一个服务否则报错
#     server.bind(('192.168.235.166',6789))
#
#     #3、开启监听--监听客户端连接到服务器
#     server.listen(512)# 参数512可以理解为连接队列的大小
#     print('服务器开启监听')
#
#     while True:
# #4.通过循环接收客户端的连接并作出相应的处理
# # accept方法是一个阻塞方法如果没有客户端连接到服务器代码不会向下执行
# # accept方法返回一个元组其中的第一个元素是客户端对象
# # 第二个元素是连接到服务器的客户端的地址(由IP和端口两部分构成)
#         client,addr = server.accept()
#         print(str(addr)+'已连接')
#         client.send(('lalalla :'+str(datetime.now())).encode('utf-8'))
#         client.close()
#
# if __name__ == '__main__':
#     main()

'''
总结：1、注意导包  2、服务端地址写本机地址，3、在客户端cmd命令里，通过Telnet 主机ip 端口号，来连接主机
4、客户端连接后服务器会打印不同的客户端连接端口号
'''
'''
客户端的写法：连接服务端与端口号，接收从服务端的信息
'''
# def client_main():
#     #1、创建套接字对象默认使用IPV4和TCP协议
#     client = socket()
#     #连接到服务器(需要指定ip地址和端口)
#     client.connect(('192.168.235.166',6789))
#     #3、从服务器接收数据
#     print(client.recv(1024).decode('utf-8'))
#     client.close()
#
# if __name__ == '__main__':
#     client_main()

'''
以上的写法，没有使用多线程或异步IO的处理方式，所以当一个客户端处于通信状态时，其他客户端只能等待排队，
   我们需要的服务器是能够同时接纳和处理多个用户请求的，

'''
# from base64 import b64encode, b64decode
# from json import dumps, loads
# from socket import socket
# from threading import Thread
#
# def main():
#
#     class FileTransferHandler(Thread):  #自定义线程类
#
#         def __init__(self,cclient):
#             super().__init__()
#             self.cclient = cclient
#
#         def run(self):
#             mydict = {}
#             mydict['filename'] = 'g.jpg'
#             mydict['filedata'] = data
#             json_str = dumps(mydict) #dumps函数将字典处理成json字符串
#             self.cclient.send(json_str.encode('utf-8'))
#             self.cclient.close()
#
#     #1、创建套接字对象并指定使用哪种传输服务
#     server = socket()
#     #2、绑定ip和端口
#     server.bind(('192.168.0.1',6789))
#     #3、开启监听
#     server.listen(512)
#     print('服务器开始启动监听....')
#     with open('g.jpg','rb') as f:
#         data = b64encode(f.read()).decode('utf-8')
#     while True:
#         client,addr = server.accept()
#         FileTransferHandler(client).start()
#
# if __name__ == '__main__':
#     main()
#
# '''
# 客户端代码
# '''
# def client_main():
#     client = socket()
#     client.connect(('192.168.0.1',5566))
#     in_data = bytes()
#     data = client.recv(1024)
#     while data :
#         in_data += data
#         data = client.recv(1024)
#
#     my_dict = loads(in_data.decode('utf-8'))
#     filename = my_dict['filename']
#     filedata = my_dict['filedata'].encode('utf-8')
#
#     with open('/user/hao'+filename,'wb') as f:
#         f.write(b64decode(filedata))
#
#     print('图片已保存')
#
# if __name__ == '__main__':
#     client_main()

'''
邮件收发：python的smtplib模块可以将邮件收发简化成几个函数
SMTP(简单邮件传输协议)是建立在TCP基础上的应用协议
'''
'''
 邮件服务端
'''
# from email.header import Header
# from email.mime.text import MIMEText
# from smtplib import SMTP
# def main():
#     sender = 'zy@zatech.com'
#     receivers = 'yu.zhang@zatech.com'
#     message = MIMEText('用python发的邮件','plain','utf-8')
#     message['From'] = Header('aa','utf-8')
#     message['To'] = Header('bb','utf-8')
#     message['Subject'] = Header('test mail','utf-8')
#     smtper = SMTP('smtp.126.com')
#
#     smtper.login(sender,'password')
#     smtper.sendmail(sender,receivers,message.as_string())
#     print('邮件发送完成')
#
# if __name__ == '__main__':
#     main()

'''
带附件的邮件
'''
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.header import Header
#
# def main():
#     message = MIMEMultipart() #创建一个带有附件的邮件消息对象
#
#     text_content = MIMEText('附件请查收','plain','utf-8')
#     message['Subject'] = Header('数据','utf-8')
#     message.attach(text_content)
#
#     with open('/user/hello.txt','rb') as f:
#         txt = MIMEText(f.read(),'base64','utf-8')
#         txt['Content-Type'] = 'text/plain'
#         txt['Content-Disposition'] = 'attachment;filename=hello.txt'
#         message.attach(txt)
#
#     with open('/user/sum.xlsx','rb') as f:
#         xls = MIMEText(f.read(),'base64','utf-8')
#         xls['Content-Type'] = 'application/vnd.ms-excel'
#         xls['Content-Disposition'] = 'attachement;filename=month-data.xlsx'
#         message.attach(xls)
#
#     smtper = SMTP('smtp.126.com')  #创建SMTP对象
#     sender = 'zy@zatech.com'
#     receivers = ['uuu@qq.com']
#     smtper.login(sender,'password')  #登录SMTP服务器
#     smtper.sendmail(sender,receivers,message.as_string()) #发送邮件
#     smtper.quit()
#     print('完成')
#
# if __name__ == '__main__':
#     main()


'''
发送短信
'''
import http
import json
import urllib

def main():
    host = '106.ihuiyi.com'
    sms_send_uri = '/webservice/sms.php?method = submit'
    params = urllib.parse.urlencode({'a':'text','p':'pwd'})
    print(params)
    headers = {'Content-type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain'}
    conn = http.client.HTTPConnection(host,port = 80,timeout = 30)
    conn.request('POST',sms_send_uri,params,headers)
    response = conn.getresponse()
    response_json= response.read().decode('utf-8')
    print(json.load(response_json))
    conn.close()

if __name__ == '__main__':
    main()