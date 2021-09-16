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
def merge(array1,array2):
    i,j,x=0,0,0
    result = []
    while i<len(array1) and j<len(array2):
        if array1[i] < array2[j]:
            result.append(array1[i])
            i += 1
        else:
            result.append(array2[j])
            j += 1

    result.append(array1[i:])
    result.append(array2[j:])
    return result

def merge_sort(array):

    if len(array) <2:
        return array

    mid = len(array)//2 #要用地板除，/会根据余数找到最近的整数

    array1 = merge_sort(array[:mid])
    array2 = merge_sort(array[mid:])
    result = merge(array1,array2)
    print(result)

if __name__ == '__main__':
    merge_sort([6,2,4,1,3,8])





