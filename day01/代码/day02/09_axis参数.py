# axis=0代表行，axis=1代表列
# 所有的数学和统计函数都有这个参数，都可以使用
# 我们想按行或按列使用时使用这个参数

import numpy as np
a = np.array([[1,3,6],[9,3,2],[1,4,3]])
print(f'数组:\n{a}')
print('-'*30)
print(np.sum(a,axis=0)) # 每行中的每个对应元素相加，返回一维数组
print(np.sum(a,axis=1)) # 每列中的每个对应元素相加，返回一维数组