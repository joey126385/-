import numpy as np
a = np.array([0,1,2,3,4,3,5,3,6,7])

# print(a.mean())
# print(a.max())
# print(a.min())

r = np.bincount(a) # 统计非负整数的个数[0,1,2,3,4,5,6]
print(r)
print(r.argmax()) # 获取众数
