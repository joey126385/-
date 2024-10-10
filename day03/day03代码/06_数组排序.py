import numpy as np

a = np.array([3, 6, 7, 9, 2, 1, 8, 5, 4])

# a.sort()
# print(a)

# 排序后 [1,2,3,4,5,6,7,8,9]
rs = np.argsort(a)  # 1的位置在a数组的下标5上,2的位置在下标4的位置,,,依次类推
print(rs)
