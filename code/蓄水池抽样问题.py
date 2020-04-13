#coding=utf-8
'''
Created on 2016年9月15日
Reservoir sampling的python实现
@author: whz
'''
import numpy as np
# import matplotlib.pyplot as plt


def pool(L,k):
    arr = L[:k]
    for i,e in enumerate(L[k:]):
        r = np.random.randint(0,k+i+1)
        if r<=k-1:
            arr[r] = e
    return arr







# def count(q,n):
#     L = array("d")
#     l1 = array("d")
#     l2 = array("d")
#     for e in q:
#         L.append(e)
#     for e in range(n):
#         l1.append(L.count(e))
#     for e in l1:
#         l2.append(e/sum(l1))
#     return l1,l2
# if __name__ == '__main__':
#     a = np.array([[i]*10000000 for i in range(3)])#生成等量的0，1，2
#     a.shape = 1,-1
#     L = a[0]
#     k = 300000#设置要抽取的样本的数量，一般远小于总体数量
#     p = pool(L, k)
#     l1 = ['value=%d'% x for x in range(3)]
#     plt.pie(count(p,3)[0],labels=l1,labeldistance=0.1,autopct='%1.2f%%')
#     plt.title("Reservoir sampling")
#     plt.show()