import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a)
print(a.shape) # (3, 3) 表示二维数组有两条轴 0轴和1轴
print(a[0:2]) # a[行切片,列切片] --> a[0轴切片,1轴切片]
print(a[0:2,1:])

x = np.arange(6).reshape(2,3).T # 行列转置 行变成列 列变成行
print(x)

# transpose()
print(x.transpose())

#  swapaxes方法【轴装置】
x1 = np.arange(24).reshape(4,6)
print(x1)
print(x1.swapaxes(1,0))
