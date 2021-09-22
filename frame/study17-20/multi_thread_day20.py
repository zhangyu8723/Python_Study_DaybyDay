'''
迭代器和生成器
  python用魔术方法表示协议
'''
#
# class Fib(object):
#     '''迭代器'''
#     def __init__(self, num):
#         self.num = num
#         self.a, self.b =0,1
#         self.idx = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.idx < self.num:
#             self.a, self.b = self.b,self.a+self.b
#             self.idx +=1
#             return self.a
#         raise StopIteration()
#
# def fib_generator(num):
#     '''生成器'''
#     a,b = 0 ,1
#     for _ in range(num):
#         a, b = b,a+b
#         yield a
import asyncio
import glob
import os
import sys
import threading
from concurrent.futures.thread import ThreadPoolExecutor
from random import randint
from time import sleep

'''
用生成器实现斐波那契数列
使用了 yield 的函数被称为生成器（generator）。
生成器是一个返回迭代器的函数，只能用于迭代操作
在调用生成器运行时，每次遇到yield会暂停并保存当前所有运行信息，返回yield的值，并在下一次执行next()时从当前位置基线运行
'''
# def fibonacci(n):  #生成器函数
#     a,b,counter = 0,1,0
#     while True:
#         if counter > n:
#             return
#         yield a
#         a,b = b,a+b
#         counter += 1
# f = fibonacci(10)   #返回一个迭代器
#
# while True:
#     try :
#         print(next(f),end=',')
#     except StopIteration:
#         sys.exit()
'''
并发编程：多线程、多进程和异步IO，
'''
# PREFIX = 'thumbnails'
# def generate_thumbnail(infile,size,format='PNG'): #"""生成指定图片文件的缩略图"""
#     file,ext = os.path.splitext(infile)
#     file = file[file.rfind('/')+1:]
#     outfile = f'{PREFIX}/{file}_{size[0]}_{size[1]}.{ext}'
#     img = Image.open(infile)
#     img.thumbnail(size,Image.ANTIALIAS)
#     img.save(outfile,format)
#
# def main():
#     if not os.path.exists(PREFIX):
#         os.mkdir(PREFIX)
#     for infile in glob.glob('images/*.png'):
#         for size in (32,64,28):
#             threading.Thread(target = generate_thumbnail,args=(infile,size,size)).start()
#
# if __name__=='__main__':
#     main()
#

'''
多线程竞争资源时，对临界资源进行加锁
'''
# import threading
# import time
# from builtins import object
# from concurrent.futures.thread import ThreadPoolExecutor
#
# class Account(object):
#     def __init__(self):
#         self.balance = 0.0
#         self.lock = threading.Lock()
#
#     def deposit(self,money):
#         with self.lock:
#             new_balance = self.balance+money
#             time.sleep(0.001)
#             self.balance = new_balance
#
# def main():
#     account = Account()
#     pool = ThreadPoolExecutor(max_workers=10)
#     threads = []
#     for _ in pool:
#         th = pool.submit(account.deposit,1)
#         threads.append(th)
#
#     pool.shutdown()
#     for t in threads:
#         t.result()
#
#     print(account.balance)
#
# if __name__ == '__main__':
#     main()
'''
线程的调度：threading模块的condition
多个线程竞争一个资源：保护临界资源 - lock(Lock/RLock)
多个线程竞争多个资源：信号量(semaphore)
多个线程的调度 - 暂停线程执行/唤醒等待中的线程 - condition
'''
# class Account:
#
#     def __init__(self , balance=0):
#         self.balance = balance
#         lock = threading.RLock()
#         self.condition = threading.Condition(lock)
#
#     def withdraw(self,money):
#         with self.condition:
#             while money > self.balance:
#                 self.condition.wait()
#         new_balance = self.balance - money
#         sleep(0.001)
#         self.balance = new_balance
#
#     def deposit(self,money):
#         with self.condition:
#             new_balance = self.balance
#             sleep(0.001)
#             self.balance = new_balance
#             self.condition.notify_all()
#
# def add_money(account):
#     while True:
#         money = randint(5,10)
#         account.deposit(money)
#         print(threading.current_thread().name,':',money,'---->',account.balance)
#         sleep(0.5)
#
# def sub_money(account):
#     while True:
#         money = randint(10, 30)
#         account.withdraw(money)
#         print(threading.current_thread().name,
#               ':', money, '<====', account.balance)
#         sleep(1)
#
# def main():
#     account = Account()
#     with ThreadPoolExecutor(max_workers = 15) as pool:
#         for _ in range(5):
#             pool.submit(add_money ,account)
#         for _ in range(10):
#             pool.submit(sub_money,account)
#
# if __name__ == '__main__':
#     main()

'''
多进程:
'''
# import concurrent.futures
# import math
#
# PRIMES=[
# 1116281,
#     1297337,
#     104395303,
#     472882027,
#     533000389,
#     817504243,
#     982451653,
#     112272535095293,
#     112582705942171,
#     112272535095293,
#     115280095190773,
#     115797848077099,
#     1099726899285419
#
# ] *5
#
# def is_prime(n):
#     #判断素数
#     if n%2 == 0:
#         return False
#
#     sqrt_n = int(math.floor(math.sqrt(n)))
#     for i in  range(3,sqrt_n+1,2):
#         if n%i == 0 :
#             return False
#     return True
#
# def main():
#     ''''''
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         for number,prime in zip(PRIMES,executor.map(is_prime,PRIMES)):
#             print('%d is prime:%s' % (number,prime))
#
# if __name__ == '__main__':
#     main()
'''
异步处理：通过`asyncio`模块和`await`和`async`关键字来支持异步处理
'''
def num_generator(m,n):
    yield from  range(m,n+1)

async  def prime_filter(m,n):
    primes = []
    for i in num_generator(m,n):
        flag = True
        for j in range(2,int(i**0.5+1)):
            if i %j ==0:
                flag = False
                break
        if flag:
            print('prim->',i)
            primes.append(i)

        await asyncio.sleep(0.001)

    return tuple(primes)

async def square_mapper(m,n):
    squares = []
    for i in num_generator(m,n):
        print('square - >',i*i)
        squares.append(i*i)

        await  asyncio.sleep(0.001)
    return squares

def main():
    """主函数"""
    loop = asyncio.get_event_loop()
    future = asyncio.gather(prime_filter(2, 100), square_mapper(1, 100))
    future.add_done_callback(lambda x: print(x.result()))
    loop.run_until_complete(future)
    loop.close()


if __name__ == '__main__':
    main()