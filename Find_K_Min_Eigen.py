# ！/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time : 2022/5/26 20:39
# Author : Xiao Chen
# @File : Find_K_Min_Eigen.py

import numpy as np

def Find_K_Min_Eigen(Matrix, Eigen_Num):
    Matrix_size = Matrix.shape
    S, V = np.linalg.eig(Matrix)
    # S = np.diag(S)
    s_temp = np.abs(S)
    index = np.argsort(s_temp)
    S = S[index]
    Eigen_Vector = np.zeros((Matrix_size[0], Eigen_Num))
    Eigen_Value = np.zeros((1, Eigen_Num))
    for t in range(0, Eigen_Num):
        Eigen_Vector[:, t] = V[:, index[t]]
        Eigen_Value[0, t] = S[t]

    return Eigen_Vector,  Eigen_Value


