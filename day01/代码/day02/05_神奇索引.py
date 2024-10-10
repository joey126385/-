import numpy as np
arr = np.arange(36).reshape(9,4)
print(arr)
print(arr[[4,3,1,6]]) # 返回第4行 第3行 第1行 以及第6行
print("================")
print(arr[[1,5,7,2],[0,3,1,2]])  # 取第一行第0列 第5行 第3列...
print("================")

# 获取数组中最大的前3个数字
arr2 = np.random.randint(1,100,10) # 10个1-100之间的随机整数
print(arr2)
# argsort() 返回排序后的下标
i = arr2.argsort()[-3:]
print(i) # 截取到最后三个索引的值
max_num = arr2[i]
#根据索引确定数组中的值
print(f'最大的三个数字是{max_num}')

