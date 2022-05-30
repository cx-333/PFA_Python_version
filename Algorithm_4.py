# ！/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time : 2022/5/25 10:47
# Author : Xiao Chen
# @File : Algorithm_4.py

import numpy as np
from Find_K_Min_Eigen import  Find_K_Min_Eigen
from compute_err import compute_err
from Algorithm_2 import Algorithm_2


def Algorithm_4(xList, sample_num, iter_num, lam_1, d_num, k):
    """
    :param xList: data of different types
    :param sample_num: number of sample
    :param iter_num:  iterator number
    :param lam_1:  超参数 lambda
    :param d_num: latent dimension
    :param k: number of data type
    :return: Y, w, L_list
    """
    w = np.ones((k*sample_num, 1)) / (k * sample_num)
    Y_final, w_final = [], []

    final_err = float('inf')
    L_list = []
    for i in range(k):
        L_list.append(0)
    # doing Algorithm 3
    for iter in range(iter_num):
        wList, sList = [], []
        for i in range(k):
            wList.append(0)
            sList.append(0)
        M = np.zeros((sample_num, sample_num))

        for i in range(k):
            temp1 = np.sqrt( w[i * sample_num : (i + 1) * sample_num, 0])
            wList[i] = np.zeros((sample_num, sample_num))
            for j in range(sample_num):
                wList[i][j, j] = temp1[j]
            ###  debug start  sList
            sList[i] = np.sum(
                np.diag(
                np.dot(
                        (np.eye(sample_num) - np.linalg.lstsq(xList[i], xList[i], rcond=None)[0]),
                        ( np.eye(sample_num) - np.linalg.lstsq(xList[i], xList[i], rcond=None)[0]).T
                                        )
                                     )
                               )
            ###  debug end

            #### debug start M
            xwList = np.linalg.lstsq(
                        np.dot(xList[i], wList[i]),
                        np.dot(xList[i], wList[i]),
                        rcond=-1
                    )[0]
            M += (1/ sList[i]) * np.dot(
                np.dot(
                    wList[i],
                    (np.eye(sample_num) - np.linalg.lstsq(
                        np.dot(xList[i], wList[i]),
                        np.dot(xList[i], wList[i]),
                        rcond=-1
                    )[0])
                       ),
                np.dot(
                    wList[i],
                    (np.eye(sample_num) - np.linalg.lstsq(
                           np.dot(xList[i], wList[i]),
                           np.dot(xList[i], wList[i]),
                           rcond=None
                       )[0])).T
            )
            ### debug end

        Y, Eigen_Value_all = Find_K_Min_Eigen(M, d_num+1)
        Y = Y[:, 1:(d_num+1)].T

        for i in range(k):
            a = np.dot(Y, wList[i])
            b = np.dot(xList[i], wList[i])
            c = np.linalg.lstsq(b.T, a.T, rcond=None)
            L_list[i] = c[0].T
        err = np.sum(
            np.diag(
            np.dot(np.dot(Y,M),
                   Y.T)
        )
        )

        if err - final_err < 0:
            final_err = err
            Y_final = Y
            w_final = w
        else:
            break

        E_list  = compute_err(w, sample_num, Y, L_list, xList, sList, k)

        w_tmp = Algorithm_2(sample_num, w, E_list, lam_1, k)
        w = w_tmp

    Y = Y_final
    w = w_final

    return Y, w, L_list

