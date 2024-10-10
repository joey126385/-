import numpy as np
a = np.array([1,2,3,4,3,5,3,6])
print(f'数组：{a}')
print(np.sum(a)) # 累加和
print(np.prod(a)) # 乘积
print(np.cumsum(a)) # 从0开始元素的累积和
print(np.cumprod(a)) # 从1开始元素的累积积
print(np.max(a))
print(np.min(a))
print(np.argmax(a)) # 最大值所在的下标
print(np.argmin(a)) # 最小值所在的下标
print(np.mean(a)) # 平均数
print(np.median(a)) # 中位数