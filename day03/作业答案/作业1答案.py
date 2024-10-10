# 作业1
import numpy as np

a1 = np.array([1, 2, 'a', 'hello', [1, 2, 3], {'two': 200, 'one': 100}], dtype=object)
print(a1.shape)
# 作业2
list1 = np.arange(5, 16)
print(list1)
# 作业3
list2 = np.zeros((4, 4))
print(list2)
list3 = np.ones((2, 3))
print(list3)
list4 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
print(list4)

# 1、创建一个长度为10的一维全为0的ndarray对象，第五个元素为1
import numpy as np
# z = np.zeros(10)
# print(z)
# z[4] = 1
# print(z)
# # 2、创建一个从10到49的ndarray对象，并实现倒叙排列
# a = np.arange(10,50)
# print(a)
# a1 = a[::-1]
# print(a1)
# # 3、使用np.random.random创建一个10*10对象，并打印出最大元素和最小元素
# b = np.random.random((10,10))
# print(b)
# print(np.max(b))
# print(np.min(b))
# # 4、创建一个10*10的ndarray对象，边界全为1，里面全为0
# b1 = np.ones((10,10))
# print(b1)
# b1[1:-1,1:-1] = 0
# print(b1)
# # 5、创建一个每一行都是0到4的5*5矩阵
# C = np.zeros((5,5))
# C += np.arange(5)
# print(C)

# 创建一个范围在（0，1）之间长度为12的等差数列
# r = np.linspace(0,1,12)
# print(r)