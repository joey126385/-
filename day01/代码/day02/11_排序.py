# ndarray.sort(axis=-1, kind='quicksort', order=None)
import numpy as np
# a = np.array([3,6,7,9,2,1,8,5,4])
# a.sort() #默认升序排序
# print(a)

#二维数组
# a = np.array([[0,12,48],[4,18,14],[7,1,99]])
# print(a)
# print(np.sort(a)) # 默认按照最后的轴排序 (0,1) 默认按照列来排序
# print(np.sort(a,axis=0)) # 按照行来排序

# numpy.argsort(a, axis=-1, kind='quicksort', order=None)
# 对数组沿给定轴执行间接排序，并使用指定排序类型返回数据的索引数组。 这个索引数组用于构造排序
# 后的数组。

import numpy as np
x = np.array([59, 29, 39])
a = np.argsort(x) # 默认都是为升序 [1 2 0] 函数返回的是数组值从小到大的索引值
print(a)

x1 = np.array([[0, 12, 48], [4, 18, 14], [7, 1, 99]])
a1 = np.argsort(x)
print(a1)