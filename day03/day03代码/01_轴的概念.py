import numpy as np

a = np.arange(5)
print(a.shape)  # (5,)表示一维数组 只有1个轴 0轴

a1 = np.arange(10).reshape(2, 5)
print(a1.shape)  # (2, 5) 有两个轴

a2 = np.array([[[2, 3, 4], [1, 2, 3]], [[4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6]]])
print(a2.shape) # (3, 2, 3)


