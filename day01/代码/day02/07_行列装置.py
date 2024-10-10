import numpy as np
arr1=np.arange(24).reshape((4,6))
print(arr1)
print("-"*30)
# print(arr1.transpose()) # reshape (6,4)
print(arr1.swapaxes(1,0)) # 轴装置 将0轴转换成1轴 1轴转换成0轴
