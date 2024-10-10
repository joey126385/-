import numpy as np

# 姓名 = np.array(['孙悟空', '猪八戒', '孙悟空', '沙和尚', '孙悟空', '唐僧'])
# print(np.unique(姓名))
# 数组 = np.array([1, 3, 1, 3, 5, 3, 1, 3, 7, 3, 5, 6])
# print(np.unique(数组))

import numpy as np
a = np.array([6,0,0,3,2,5,6])
print(np.in1d(a,[2,3,6])) # 检查是否出现在数组a中