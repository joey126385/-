# axis=0代表行，axis=1代表列

import numpy as np

a = np.array([[1, 3, 6], [9, 3, 2], [1, 4, 3]])
print(a)
# print(np.sum(a))  # 32
print(np.sum(a, axis=0)) # [11 10 11]
print(np.sum(a, axis=1)) # [10 14  8]

# 其中思路正好是反的：axis=0 求每列的和。axis=1求每行的和。
