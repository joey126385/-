# 使用ones()创建全是1的数组
# shape：整数或者整型元组定义返回数组的形状；可以是一个数（创建一维向量），也可以是一个元组（创建
# 多维向量）
# dtype : 数据类型，可选定义返回数组的类型
import numpy as np
a = np.ones(3,dtype=np.int32)
b = np.ones((3,2),dtype=np.int32) # (3,2) 这是一个元组 表示3行2列的数组形状
print(b)


# np.ones_like(a,dtype=float,order='C',subok=True)
# 返回：与a相同形状和数据类型的数组，并且数组中的值都为1
new_arr = np.ones_like(b,dtype=np.float32)
print(new_arr)


# np.full(shape,fill_value,dtype=None,order='C')
# 参数：
# shape：整数或者整型元组定义返回数组的形状；可以是一个数（创建一维向量），也可以是一个元组（创建
# 多维向量）
# fill_value：标量（就是纯数值变量）
# dtype : 数据类型，可选定义返回数组的类型。

arr1 = np.full((3,4),fill_value=520,dtype=np.int32)
print(arr1)



# full_like创建开关相同的指定值数组
arr2 = np.full_like(arr1,fill_value=12)
print(arr2)

lst = [1,23,3,4,5]
lst2 = [[1,2,3,4],[2,3,4,5]] # 二维数组
lst3 = [[[],[],[]],[[],[],[]]] # 三位数组
