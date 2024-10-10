import numpy as np
arr1 = np.arange(1,21).reshape(4,5)
print(arr1)
test = arr1>10
print(test) # 返回一个4行5列的布尔数组 有行有列
print(arr1[test]) # 将索引为True的值组成一个一维数组返回 [11 12 13 14 15 16 17 18 19 20]

# 例：把第3列大于5的行筛选出来并重新赋值为520
# 先取出所有行的第三列
print(arr1[:,2])
test = arr1[:,2]>5
arr1[arr1[:,2]>5] = 520
print(arr1)