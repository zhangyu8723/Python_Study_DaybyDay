'''
- 算法：解决问题的方法和步骤
- 评价算法的好坏：渐近时间复杂度和渐近空间复杂度。
- 渐近时间复杂度的大O标记：
  - O(C) - 常量时间复杂度 - 布隆过滤器 / 哈希存储
  - O(log2n)- 对数时间复杂度 - 折半查找（二分查找）
  - O(n)- 线性时间复杂度 - 顺序查找 / 计数排序
  - O(n *log2n)- 对数线性时间复杂度 - 高级排序算法（归并排序、快速排序）
  - O(n^2) - 平方时间复杂度 - 简单排序算法（选择排序、插入排序、冒泡排序）
  - O(n^3)- 立方时间复杂度 - Floyd算法 / 矩阵乘法运算
  - O(2^n) - 几何级数时间复杂度 - 汉诺塔
  - O(n!)- 阶乘时间复杂度 - 旅行经销商问题 - NPC
'''

'''
排序算法(选择、冒泡和归并) 和查找算法(顺序和折半)
选择算法：选择一个数与右边相比，右边的小于当前数则交换位置，每次产生一个最小数在左边
'''
# def select_sort(arrys,comp=lambda x,y : x<y):
#
#     for i in range(len(arrys)-1):
#         min = i
#         for j in range(i+1,len(arrys)):
#             if comp(arrys[j] , arrys[min]):
#                 min = j
#         arrys[min],arrys[i] = arrys[i],arrys[min]
#     print(arrys)
#     return arrys
#
# if __name__ == '__main__':
#      arrys = [5,2,0,1,8]
#      result = select_sort(arrys)
#      print(result)
'''
冒泡算法:i控制次数，j从0开始，与j+1进行比较，j>j+1交换，每次产生一个最大数在后面
   若每次都有交换，说明序列已排好，直接中断
'''
# def buble_sort(arrys,comp = lambda x,y :x > y):
#
#     for i in range(len(arrys)-1):
#         swap = False
#         for j in range(len(arrys)-1-i):
#             if comp(arrys[j],arrys[j+1]):
#                 arrys[j],arrys[j+1] = arrys[j+1],arrys[j]
#                 swap = True
#         if not swap:
#             break
#
#     print(arrys)
# if __name__ == '__main__':
#     buble_sort([4,9,0,1,3])
'''
归并排序：先将一个数组拆分成两个数组，然后按小到大进行合并
'''
# def merge(array1,array2):
#     i,j,x=0,0,0
#     result = []
#     while i<len(array1) and j<len(array2):
#         if array1[i] < array2[j]:
#             result.append(array1[i])
#             i += 1
#         else:
#             result.append(array2[j])
#             j += 1
#
#     result+=array1[i:]
#     print("result1:",result)
#     result+=array2[j:]
#     print("result2:", result)
#     return result
#
# def merge_sort(array):
#
#     if len(array) < 2:
#         return array
#
#     mid = len(array) // 2 #要用地板除，/会根据余数找到最近的整数
#
#     array1 = merge_sort(array[:mid])
#     array2 = merge_sort(array[mid:])
#
#     return merge(array1,array2)
#
#
# if __name__ == '__main__':
#     merge_sort([6,2,4,1,3,8])

'''
总结：列表的append()是在原列表中进行拼接
      列表的+ 是重新生成列表后添加，不对原列表进行修改
'''
'''
穷举法:又称为暴力破解法，对所有的可能性进行验证，直到找到正确答案
百钱白鸡：公鸡5元一只 母鸡3元一只 小鸡1元三只,用100元买100只鸡 问公鸡/母鸡/小鸡各多少只?
'''
# def buy_chicken():
#     for i in range(20):
#         for j in range(33):
#             y = 100 - i -j
#             if 5*i + 3*j +y//3 == 100 and y%3 ==0 :
#                print('公鸡 %d只，母鸡%d只，小鸡%d' % (i,j,y))
#
# if __name__ == '__main__':
#     buy_chicken()
'''
A、B、C、D、E五人在某天夜里合伙捕鱼 最后疲惫不堪各自睡觉
# 第二天A第一个醒来 他将鱼分为5份 扔掉多余的1条 拿走自己的一份
# B第二个醒来 也将鱼分为5份 扔掉多余的1条 拿走自己的一份
# 然后C、D、E依次醒来也按同样的方式分鱼 问他们至少捕了多少条鱼
'''
# def main():
#     fish = 6
#     while True:
#         total = fish
#         flag = True
#         for _ in range(5):
#             if (total - 1) % 5 == 0:
#                 total = (total-1)/5 * 4
#             else:
#                 flag = False
#                 break
#         if flag:
#             print(fish)
#             break
#         fish += 5
#
# if __name__ == '__main__':
#     main()
'''
小偷偷钱
'''
# class product():
#     def __init__(self,name,price,weight):
#         self.name = name
#         self.price = price
#         self.weight = weight
#
#     @property
#     def value(self):
#         return self.price /self.weight
#
# def input_str():
#     name,price,weight = input().split()
#     return name,int(price),int(weight)
#
# def main():
#     max_weight,num = map(int,input().split())
#     all_things = []
#     for _ in range(num):
#         all_things.append(product(*input_str()))
#
#     all_things.sort(key=lambda  x :x.value,reverse=True)
#     total_weight = 0
#     total_price = 0
#     for thing in all_things:
#         if total_weight + product.weight <= max_weight:
#             print(f'小偷拿走了{product.name}')
#             total_weight+=product.weight
#             total_price+=product.price
#
#     print(f'总价值:{total_price}元')
#
#
# if __name__ == '__main__':
#     main()
'''
快速排序：对元素进行划分，左边都比目标值小，右边都比目标值达
'''
# def quick_array(array,start,end):
#    if start < end :
#         pos = partition(array,start,end)
#         quick_array(array,start,pos-1)
#         quick_array(array,pos+1,end)
#
# def partition(array,start,end):
#     pivot = array[end]
#     i = start -1
#     for j in range(start,end):
#         if array[j] < pivot:
#             i += 1
#             array[i],array[j] = array[j],array[i]
#
#     array[i+1],array[end] = array[end],array[i+1]
#     return i+1
#
# if __name__ == '__main__':
#     list = [6,4,0,2,1,3]
#     quick_array(list,0,5)
#     print(list)

'''
总结：
1、终止条件 start<end很重要
2、思想：选择最后一个数为目标数，遍历数组比目标数小的在左边，i++，比目标数大的，不变，最后目标数和i+1交换，
确定了目标数的位置
'''
'''
回溯法:按选优条件向前搜索，当搜索到某一步，发现原先选择并不优或达不到目标时，就退回一步重新选择
'''

# SIZE = 5
# total = 0
# def print_board(board):
#     for row in board:
#         for col in row:
#             print(str(col).center(4),end='')
#         print()
#
# def patrol(board,row,col,step=1):
#     if row >= 0 and row <SIZE and col >=0 and col <SIZE and \
#         board[row][col] == 0:
#         board[row][col] = step
#         if step == SIZE * SIZE:
#             global total
#             total += 1
#             print(f'第{total}种走法: ')
#             print_board(board)
#         patrol(board, row - 2, col - 1, step + 1)
#         patrol(board, row - 1, col - 2, step + 1)
#         patrol(board, row + 1, col - 2, step + 1)
#         patrol(board, row + 2, col - 1, step + 1)
#         patrol(board, row + 2, col + 1, step + 1)
#         patrol(board, row + 1, col + 2, step + 1)
#         patrol(board, row - 1, col + 2, step + 1)
#         patrol(board, row - 2, col + 1, step + 1)
#         board[row][col] = 0
#
# def main():
#     board = [[0] * SIZE for _ in range(SIZE)]
#     patrol(board ,SIZE-1,SIZE-1)
#
# if __name__ == '__main__':
#     main()

'''
动态规划：基本思想也是将待求解问题分解成若干个子问题，先求解并保存这些子问题的解，避免产生大量的重复运算。
# '''
# def main():
#     items = list(map(int,input().split()))
#     overall = partial = items[0]
#     for i in range(1,len(items)):
#         partial = max(items[i] , partial + items[i])
#         overall = max(partial,overall)
#     print(overall)
#
# if __name__ == '__main__':
#     main()


