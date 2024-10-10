# reshape不改值修改形状
import numpy as np
a = np.arange(10).reshape(2,5)
print(a)
#变成一行一列
b = a.reshape(10)
print(b)
#不管维度是多少 直接转换成1维
c = a.flatten()
print(c)