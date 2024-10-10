import numpy as np

lst1 = [i for i in range(20)]
lst2 = [i for i in range(21, 41)]
# print(lst1+1)
# print(lst1+lst2)


# 二维数组
# 数组的好处:直接进行数学运算
# a = np.arange(20).reshape(4, 5)
a = np.arange(10).reshape(2, 5)
print(a)

# print(a + 1)
#
# print(a * 3)

# 1.形状相同的两个数组 能否直接运算? 可以直接参与运算
b = np.random.randn(2, 5)
print(b)
print(a+b)


# 2.形状不同数组
