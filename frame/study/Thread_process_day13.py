'''
进程:操作系统中执行的程序，操作系统以进程为单位分配存储空间，   每个进程都有自己的地址空间、数据栈，以及用于跟踪进程执行的辅助数据。
     进程可以通过fork和spawn来创建新的进程，
     进程间通信方式(IPC,inter-process communication)，管道、信号、套接字、共享内存区

python的并发编程方式：多进程、多线程、多进程+多线程
'''
# from multiprocessing import Process
# from os import getpid
# from random import randint
# from time import sleep, time
#
#
# def task(taskName):
#     print('开始%s任务----任务id:%d' % (taskName,getpid()))
#     time = randint(1,5)
#     sleep(time)
#     print('----%s任务结束' % taskName)
#
# def createMutilProcess():
#     start = time()
#     p1 = Process(target=task,args=('study python',))  # 开启一个进程
#     p1.start()   #开启进程
#     p2 = Process(target=task,args=('work test',))
#     p2.start()
#     p1.join()    #等待进程结束
#     p2.join()
#     end = time()
#     print('共耗时%d' % (end-start))
#
# if __name__ == '__main__':
#     createMutilProcess()
# import tkinter
# from os import getpid
# from random import randint
# from threading import Thread
# from time import sleep, time

'''
扩展：①可以通过subprocess模块中的类和函数来创建和启动子进程
     ②multiprocessing模块中的Queue类，可以被多个进程共享队列
'''

'''
多线程:导入threading模块、或者继承Thread类
'''


#
# class multiThread(Thread):
#      def __init__(self,taskName):
#          super().__init__()
#          self._taskName = taskName
#
#      def run(self):
#          print('---%s任务开启,进程号:%d..' % (self._taskName , getpid()))
#          time = randint(1,5)
#          sleep(time)
#          print('---%s任务结束..' % (self._taskName))
#
#
# def createMultiThread():
#     start = time()
#     t1=multiThread('study python')
#     t1.start()
#
#     t2=multiThread('work test')
#     t2.start()
#     t1.join()
#     t2.join()
#     end = time()
#     print('任务结束，共耗时:%d' % (end-start))
#
# if __name__ == '__main__':
#     createMultiThread()
'''
总结：1、实例化继承Thread类的时候，就相当于创建了多线程，
      2、join()方法相当于 线程会等待进程结束，线程才会结束
      3、实例化的时候要实例化父类的init方法,super().__init__()
'''
'''
使用多线程对临界资源进行调用
'''
# from threading import Thread, Lock
# class Account():
#     def __init__(self):
#         self._balance = 0
#         self._lock = Lock()  #将lock成为属性
#
#     def deposit(self,money):
#          self._lock.acquire()  #先获得锁才能执行后面代码
#          try:
#             newBalance = self._balance + money
#             sleep(0.01)
#             self._balance = newBalance
#          finally:
#             self._lock.release()  #释放锁
#
#
#     @property
#     def balance(self):
#         return self._balance
#
# class AddMondy(Thread):
#     def __init__(self,account,money):
#         super().__init__()
#         self._account = account
#         self._money = money
#
#     def  run(self):
#         self._account.deposit(self._money)
#
#
# def main():
#     account = Account()
#     threadlist = []
#     for x in range(100):   #先创建100个线程放进列表里
#        t = AddMondy(account,1)
#        threadlist.append(t)
#        t.start()
#     for t in threadlist:
#         t.join()
#     print('get balance %.2f' % account.balance)
#
# if __name__ == '__main__':
#     main()
'''
总结：1、锁通过属性的形式添加到对象里
      2、通过lock().acquire()方式获得锁
      3、在finally里release()释放锁
'''
'''
单线程+异步IO： 在python中单线程+异步IO的编程模型称之为协程
      优势：①执行效率高， 不需要线程切换，而是由程序自身控制的子程序切换，所以没有线程切换的开销
           ②不需要多线程的锁机制，由于只有一个线程，没有写冲突，不用加锁，执行效率会高很多
'''
# import time
# import tkinter
# import tkinter.messagebox
# from threading import Thread
#
# def main():
#     class TaskHandler(Thread):
#         def run(self):
#             time.sleep(2)
#             tkinter.messagebox.showinfo('提示','down ok')
#             button1.config(state=tkinter.NORMAL)
#
#     def download():
#         button1.config(state = tkinter.DISABLED) #禁用下载按钮
#         TaskHandler(daemon=True).start()
#
#     def show():
#         tkinter.messagebox.showinfo('show','me')
#
#     top = tkinter.Tk()
#     top.title('单线程')
#     top.geometry('200x150')
#     top.wm_attributes('-topmost',1)
#
#     panel = tkinter.Frame(top)
#     button1 = tkinter.Button(panel, text='下载', command=download)
#     button1.pack(side='left')
#     button2 = tkinter.Button(panel, text='关于', command=show)
#     button2.pack(side='right')
#     panel.pack(side='bottom')
#
#     tkinter.mainloop()
#
# if __name__ == '__main__':
#     main()
'''
练习：完成1~100000000求和的计算密集型任务
'''
from multiprocessing import Process, Queue
from time import time


def countNum(numlist,result_queue):
    count = 0
    for x in numlist:
        count += x
    result_queue.put(count)

def main():
    numlist = [x for x in range(1,1000001)]
    result_queue = Queue()
    processlist = []
    index = 0
    leng = 125000

    for _ in range(8):
        p1 =Process(target=countNum,args=(numlist[index:index+leng] , result_queue))
        processlist.append(p1)
        index = index + leng
        p1.start()


    start = time()
    for p in processlist:
        p.join()

    totle = 0
    while not result_queue.empty():
        totle += result_queue.get()

    print("totle:%d" % totle)
    end = time()
    print('共耗时:' , (end-start))

if __name__ == '__main__':
    main()

