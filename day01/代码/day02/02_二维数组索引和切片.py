import numpy as np
arr = np.arange(20).reshape(4,5)
print(arr)
print(arr[0,0]) # 如果是对二维数组进行索引和切片操作的话 语法: 数组名称[行索引,列索引]
print(arr[-1,2]) # 最后一行 第二列 17
print(arr[-1]) # 最后一行 所有的值

#切片操作 数组名称[行切片,列切片]
print(arr[0:-1]) # 除了最后一行以外所有的行
print(arr[0:2,2:4]) # 0行和1行 2和3列
print(arr[:,2]) # 取所有行中的第二列


#创建10*10的全为0数组
arr1 = np.zeros((10,10))
print(arr1)
#修改每一行的第一个元素的值为520
arr1[:,0] = 520
print(arr1)
#修改中间四列的值为888
arr1[:,3:7] = 888
print(arr1)