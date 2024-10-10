# 一维数组 布尔索引
import numpy as np
arr = np.arange(10)
print(arr)
#通过布尔索引筛选出大于5的值
rs = arr>5
# rs结果中就包含了布尔索引
print(arr[rs]) # 6 7 8 9

# 实例1：把一维数组进行01化处理
# 将数组中大于5的数字变成1 小于等于5的数字变成0
# arr[arr<=5] = 0
# arr[arr>5] = 1
# print(arr)

# 进行自增量的操作，给大于5的加上520
arr[arr>5] +=520
print(arr)

#二维数组

