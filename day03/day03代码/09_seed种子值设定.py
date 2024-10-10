import random
import numpy as np

np.random.seed(101)
print(np.random.random())
np.random.seed(101)
print(np.random.random())

# pip install pandas -i https://pypi.tuna.tsinghua.edu.cn/simple
# 如果出现安装错误
# 1.pip 版本更新
# 2.time out 错误 加上镜像源解决