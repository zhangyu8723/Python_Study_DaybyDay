'''
生成式(推导式)的用法: param= {k,v for k,v in prices.items() if v > 100}
'''
# prices = {
#     'AAPL': 191.88,
#     'GOOG': 1186.96,
#     'IBM': 149.24,
#     'ORCL': 48.44,
#     'ACN': 166.89,
#     'FB': 208.09,
#     'SYMC': 21.29
# }
# #过滤value大于100的数据，组成新的dict
# param ={ k:v for k,v in prices.items() if v >= 100 }
#
# print(param)
'''
嵌套列表
输入
'''
# names = ['关羽', '张飞', '赵云', '马超', '黄忠']
# courses = ['语文','数学','英语']
#
# scores =[[None] * len(courses) for _ in  range(len(names))]
# print(scores)   #[[None, None, None], [None, None, None], [None, None, None], [None, None, None], [None, None, None]]
#
# for row,name in enumerate(names):
#     for col,course in enumerate(courses):
#         scores[row][col] = float(input(f'请输入{name}的{course}成绩'))
#         print(scores)
# print('完整:',scores)
'''
总结:1、先创建3行 5列的二维数组， (None * 行数) * 逐一乘以列数，不能直接乘以列数
     2、enumerate()返回列表的下标和值，['a','b','c']返回[(0:a),(1:b),(2:c)]
'''
'''
堆排序： heapq模块,
'''
# import heapq
#
# list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
# list2 = [
#     {'name': 'IBM', 'shares': 100, 'price': 91.1},
#     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#     {'name': 'FB', 'shares': 200, 'price': 21.09},
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
#     {'name': 'ACME', 'shares': 75, 'price': 115.65}
# ]
# print(heapq.nlargest(len(list1), list1))  #从大到小排序[99, 92, 88, 87, 78, 63, 58, 34, 25, 12]
# print(heapq.nsmallest(len(list1),list1))  #从小到大排序[12, 25, 34, 58, 63, 78, 87, 88, 92, 99]
# print(heapq.nlargest(2,list2,key = lambda x:x['price']))  #[{'name': 'AAPL', 'shares': 50, 'price': 543.22}, {'name': 'ACME', 'shares': 75, 'price': 115.65}]
# print(heapq.nsmallest(2,list2,key = lambda x:x['shares']))  #[{'name': 'HPQ', 'shares': 35, 'price': 31.75}, {'name': 'YHOO', 'shares': 45, 'price': 16.35}]
'''
总结：1、heapq可以直接根据传入的值，进行大根堆、小根堆排序
      2、根据lambda表达式对对象进行排序
'''
'''
迭代工具：itertools模块
'''
import itertools

# 产生ABCD的全排列
# for x in itertools.permutations('ABCD'):
#     print(x)

#产生ABCDE 5选3全排
# for x in itertools.combinations('ABCDE',3)  :
#     print(x)
#产生ABC和123的笛卡尔积
# for x in itertools.product('ABC','123'):
#     print(x)

#无限循环
# for x in itertools.cycle('abc'):
#     print(x)

'''
collection模块，
- `namedtuple`：命令元组，它是一个类工厂，接受类型的名称和属性列表来创建一个类。
- `deque`：双端队列，是列表的替代实现。Python中的列表底层是基于数组来实现的，而deque底层是双向链表，因此当你需要在头尾添加和删除元素是，deque会表现出更好的性能，渐近时间复杂度为$O(1)$。
- `Counter`：`dict`的子类，键是元素，值是元素的计数，它的`most_common()`方法可以帮助我们获取出现频率最高的元素。`Counter`和`dict`的继承关系我认为是值得商榷的，按照CARP原则，`Counter`跟`dict`的关系应该设计为关联关系更为合理。
- `OrderedDict`：`dict`的子类，它记录了键值对插入的顺序，看起来既有字典的行为，也有链表的行为。
- `defaultdict`：类似于字典类型，但是可以通过默认的工厂函数来获得键对应的默认值，相比字典中的`setdefault()`方法，这种做法更加高效。
'''
'''
找出序列中出现次数最多的元素
'''
# from  collections import  Counter
#
# words = [
#     'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
#     'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
#     'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
#     'look', 'into', 'my', 'eyes', "you're", 'under'
# ]
# counter = Counter(words)
# print(counter.most_common(3))   #[('eyes', 8), ('the', 5), ('look', 4)]