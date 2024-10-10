import pandas as pd

# 演示 数据的读取

lj = r'D:/pandas_/读取文件.csv'
# lj = r'D:/pandas_/读取文件.xlsx'

# 读取数据
# df = pd.read_csv(lj,encoding='gb2312') # 默认使用utf-8读取文件
# df = pd.read_excel(lj) # 默认使用utf-8读取文件 xlrd

# 读取数据 指定列名
# df = pd.read_excel(lj,header=None,names=['姓名','年龄','tel','addr','rate_time'],sheet_name=0) # 默认使用utf-8读取文件 xlrd
df = pd.read_csv(lj,sep=',',header=None,names=['姓名','年龄','tel','addr','rate_time'],encoding='gb2312') # 默认使用utf-8读取文件 xlrd

print(df)

# df.to_excel(lj)

# print(df)
