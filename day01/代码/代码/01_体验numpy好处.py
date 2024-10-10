# 题目： 数组a与数组b相加，数组a是1~N数字的立方，数组b是1~N数字的平方
def arr_add(n):
    a = [i**3 for i in range(1,n+1)]
    b = [i**2 for i in range(1,n+1)]
    c = []
    for i in range(n):
        c.append(a[i]+b[i])
    return c

lst = arr_add(4)
print(lst)

#使用numpy实现两个数组相加
import numpy as np #取别名
def arr_add2(n):
    a = np.arange(1,n+1)**3
    b = np.arange(1,n+1)**2
    return a+b

lst1 = arr_add2(4)
print(lst1)


