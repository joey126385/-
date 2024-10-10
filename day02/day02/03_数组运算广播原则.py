import numpy as np

# 数组的维度不同，后缘维度的轴长相符，是可以进行运算



# 2*5的二维数组
a = np.arange(10).reshape(2,5)
print(a) # (2,5)

# 1*5的一维数组
# b = np.arange(5)
# print(b) # (,5)
#
# # 对两个数组进行加法运算
# print(a+b) # 可以进行运算

b1 = np.arange(4).reshape(2,2)
print(b1)
# print(a+b1) # 不支持运算

#总结:
# 数组与数组之间运算的原则:
# 1.数组的形状相同 可以直接进行运算 a (2,5) b(2,5)
# 2.数组的维度不同，但是数组的后缘维度相同的情况下，也是可以支持运算 a(2,5) b(,5)
# 3.数组的维度相同，期中有一个数组的长度为1，可以支持运算 a(4,3) b(4,1)

x = np.array([[1,2,3],[4,5,6]])
# y = np.array([[1,1,1],[1,1,1],[1,1,1]])
y = np.array([[1,2,3]])
print(y.shape)
# print(x.ndim) # 2
# print(y.ndim) # 2
print(x+y)
