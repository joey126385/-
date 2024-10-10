import numpy as np

a = np.arange(10)
print(a)

# 1,筛选出数组中大于5的元素
f = a > 5
print(f)  # [False False False False False False  True  True  True  True] 布尔索引
# 根据布尔索引进行筛选
# print(a[f])
# 简写
print(a[a > 5])

# 实例: 将大于5的自增 加上100
a[a > 5] += 100
print(a)
