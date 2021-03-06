import numpy as np

'''
加权平均数和算数平均数：
1、简单的算术平均数的计算公式为：
M = (X1+X2+...+Xn)/n
加权平均数的公式如下，w为各个事件的概率
x = (x1w1 + x2w2 + x3w3 +...+ xnwn)/(w1+w2+...+wn)
2、用法不同：在实际问题中，当各项权重不相等时，计算平均数时就要采用加权平均数；当各项权相等时，计算平均数就要采用算术平均数。

3、影响因素不同：

加权算术平均数同时受到两个因素的影响，一个是各组数值的大小，另一个是各组分布频数的多少。在数值不变的情况下，一组的频数越多，该组的数值对平均数的作用就大，反之，越小。

算术平均数易受极端值的影响。例如有下列资料：5、7、5、4、6、7、8、5、4、7、8、6、20，全部资料的平均值是7.1，实际上大部分数据（有10个）不超过7，如果去掉20，则剩下的12个数的平均数为6。
'''
# 需要求加权平均数的列表
elements = [1, 2, 3, 4, 5, 6, 7]
# 权重
weights = [0.1, 0.2, 0.3, 0.1, 0.1, 0.1, 0.1]
# 求加权平均数
average_weight = np.average(elements, weights=weights)


# 算数平均数的方法
def get_ave(ele, wei):
    return sum(ele) / len(wei)


# 加权平均数的方法
def get_ave_wei(ele, wei):
    return np.average(ele, weights=wei)


print("加权前： ", get_ave(elements, weights))
print("加权后： ", get_ave_wei(elements, weights))
