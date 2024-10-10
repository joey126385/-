# import numpy as np
# a = np.array([[1,3,6],[9,3,2],[1,4,3]])
#
# # 统计数组中大于3的个数有多少
# print((a>3).sum())
#
# print(np.where(a>3,520,1234))

import numpy as np

a = np.array([False, False, True, False])
print(a.any())  # 检查数组中最少有一个为True
print(a.all())  # 检查数组中是否所有值都为True
