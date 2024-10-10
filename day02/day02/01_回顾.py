# 1.回顾数组的创建

import numpy as np

# 方式一
a = np.array([1,2,3,4,5,6])
print(type(a)) # numpy.ndarray
# 方式二
a1 = np.array(range(1,101))
print(a1)
# 方式三
a2 = np.arange(101,2,step=-1)
print(a2)

# 数组的属性介绍
a3 = np.array([[1,2,3],[4,5,6]])
print(a3.shape)# (2, 3)
print(a3.ndim) # 数组的维度
print(a3.size) # 6
print(a3.dtype) # 元素类型 int32

