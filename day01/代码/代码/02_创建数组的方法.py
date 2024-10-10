import numpy as np
a = np.array([1,2,3,4,5])
b = np.array(range(1,11)) # 创建一个1-10范围的数组
c = np.arange(1,6)
print(a) # [1 2 3 4 5]
# print(type(a)) # numpy.ndarray
# print(b)
# print(c)
# print(type(c)) # numpy.ndarray

#数组常用属性
# • shape：返回一个元组，表示 array的维度 [形状，几行几列] （2，3）两行三列，（2，2，3）两个两
# 行三列
# • ndim：返回一个数字，表示array的维度的数目
# • size：返回一个数字，表示array中所有数据元素的数目
# • dtype：返回array中元素的数据类型
print(a.shape) # 一维数组
print(a.ndim) # 1
print(a.dtype) # int32


# arange创建数字序列
# np.arange([开始,]结束[,步长],dtype=None)
arr2 = np.arange(1,20,2,dtype=np.int32)
print(arr2)

