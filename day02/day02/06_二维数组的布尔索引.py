import numpy as np

x = np.arange(1, 21).reshape(4, 5)
print(x)

# print(x > 10)
# # 根据布尔索引进行筛选
# print(x[x > 10])

# 将第三列大于5的行筛选出来重新赋值为520
r = x[:, 3] > 5

x[x[:, 3] > 5,3] = 520
print(r.shape)
print(x) #
