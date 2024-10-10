# import random
import numpy as np


# print(random.random()) # 0-1之间随机浮点数

# print(np.random.rand())

a = np.random.choice(10,3) # 生成一个长度为3的一维数组 10表示生成范围是0-10
# print(a)

a1 = np.random.choice([1,3,4,6,7,8,11],(2,3))
# print(a1)

x = np.arange(10)
np.random.shuffle(x) # 随机排序
print(x)

