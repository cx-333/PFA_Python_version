# ！/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time : 2022/5/27 13:06
# Author : Xiao Chen
# @File : compute_err.py

import numpy as np

def compute_err(w, sample_num, Y, L_list, xList, sList, k):
    """
    :param w:  correction Matrix   ([w1, w2, ..., wm])
    :param sample_num:  the number of sample
    :param Y:  sample-spectrum Matrix
    :param L_list: 1x3 cell
    :param xList:  1x3 cell
    :param sList:  1x3 cell
    :param k:  the number of data type
    :return:  E_list 1x3 cell
    """
    E_list = []
    for i in range(k):
        E_list.append(0)

    E_list_1, E_list_2, E_list_3 = [], [], []
    for i in range(sample_num):
        for j in range(k):
            x_j = xList[j]
            if j == 0:
                E_list_1.append((1/sList[j]) * w[j * sample_num + i, 0] * np.dot((Y[:, i] -
                        np.dot(L_list[j], x_j[:, i])).T, (Y[:, i] - np.dot(L_list[j], x_j[:, i]))))
            elif j == 1:
                E_list_2.append((1/sList[j]) * w[j * sample_num + i, 0] * np.dot((Y[:, i] -
                        np.dot(L_list[j], x_j[:, i])).T, (Y[:, i] - np.dot(L_list[j], x_j[:, i]))))
            else:
                E_list_3.append((1/sList[j]) * w[j * sample_num + i, 0] * np.dot((Y[:, i] -
                        np.dot(L_list[j], x_j[:, i])).T,  (Y[:, i] - np.dot(L_list[j], x_j[:, i]))))

    E_list[0] = np.array([E_list_1]).T
    E_list[1] = np.array([E_list_2]).T
    E_list[2] = np.array([E_list_3]).T

    return E_list

# wYL_listxList = io.loadmat('wYL_listxList.mat')
# E_list_compute = io.loadmat('E_list_compute.mat')
#
# L_list = wYL_listxList['L_list']
# Y = wYL_listxList['Y']
# w = wYL_listxList['w']
# xList = wYL_listxList['xList']
# print(L_list.shape)
# print(Y.shape)
# print(w.shape)
# print(xList.shape)
# sList = [321, 300, 350]
# Llist = [0, 0, 0]
# xlist = [0, 0, 0]
# for i in range(len(Llist)):
#     Llist[i] = L_list[0, i]
#     xlist[i] = xList[0, i]
#
# elist = compute_err(w=w, sample_num=100, Y=Y, L_list=Llist, xList=xlist, sList=sList, k=3)
# print(elist, E_list_compute)
# with open('compute_err.txt', 'w', encoding='utf-8') as f:
#     f.write('Python: \n' + 'E_list:' )
#     f.write(str(elist))
#     f.write('Matlab: \n' + 'E_list:')
#     f.write(str(E_list_compute))

