# 创建一个10*10的0数组
import numpy as np
z = np.zeros((10,10))
print(z)

# 创建一个长度为10的0数组，第5个值为1
z = np.zeros(10)
z[4] = 1
print(z)
# 创建一个值从10到49的数组
z = np.arange(10,50)
print(z)
# 反转数组（第一个元素变成最后一个）
Z = z[::-1]
print(Z)

# 创建一个从0~8的3*3矩阵
a = np.arange(9).reshape(3,3)
print(a)
# 从[1,2,0,0,4,0]中找到非0元素的索引
b = [1,2,0,0,4,0]
nz = np.nonzero(b)
print(nz)
# 创建一个10*10的随机值数组，并找到最大最小值
Z = np.random.random((10,10))
print(Z)
Z_max = Z.max()
Z_min = Z.min()
print(Z_max,Z_min)


# 创建一个长度为30的随机值数组，并找到平均值
Z = np.random.random(30)
m = Z.mean()
print(m)
# 创建一个四边为1，中间为0的二维数组，
Z = np.ones((10,10))
Z[1:-1,1:-1] = 0
print(Z)
# 创建一个5*5的矩阵，每一行值为0~4
Z = np.zeros((5,5))
Z+=np.arange(5)
print(Z)
# 创建一个长度为10的数组，并做排序操作
Z = np.random.random(10)
Z.sort()
print(Z)