import pandas as pd  # 取别名为pd

# 1.创建空的表格

# df = pd.DataFrame()

# 写入数据到表格中
df = pd.DataFrame({'id': [1, 2, 3], 'name': ['zs', 'lisi', '条条']})

# 2.将空白的表格写入到文件中
# lj = r'D:/pandas_/demo1.xlsx'  # 绝对路径
# lj = 'data_/demo.xlsx'
lj = 'data_/demo1.csv'
# df.to_excel(lj)
df.to_csv(lj)

print('文件创建成功')
