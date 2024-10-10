# import numpy as np
# a = np.arange(10).reshape(2,5)
# print(a)
#
# #对数组进行数学运算
# print(a+1) # 对二维数组中每一个元素都进行+1操作
# print(a*3) #

import numpy as np
import random
a = np.arange(10).reshape(2,5)
# b = np.random.randn(2,5)
b = np.arange(11,21).reshape(2,5)
print(b)
# 对形状相同的数组 进行数学运算
print(a+b)

# （1）形状一样的数组按对应位置进行计算。
# （2）一维和多维数组是可以计算的，只要它们在某一维度上是一样的形状，仍然是按位置计算。