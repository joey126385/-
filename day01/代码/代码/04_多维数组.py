import numpy as np

a = np.array(range(1, 7))
print(a)
b = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(b)
print(b.shape)  # (2,3)
print(b.ndim)  # 2

# 得到一个三维数组
n1 = np.array(
    [[[1, 2], [3, 4]], [[5, 6], [7, 8]],[[9,10],[11,12]]]
)
print(n1.shape) # (3, 2, 2)
