# ！/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time : 2022/5/26 15:55
# Author : Xiao Chen
# @File : Algorithm_2.py

from Find_K_Min_Eigen import Find_K_Min_Eigen
import numpy as np

def Algorithm_2(sample_num, w, E_list, lam_1, k):
    """
    :param sample_num:  the number of sample
    :param w:  dimension--(k * sample_num, 1) , correction matrix
    :param E_list: [E_list1, E_list2, E_list3]   E_listx dimension--(sample_num, 1)
    :param lam_1: tuning parameter, default lam_1 = 1
    :param k:  the number of different data type
    :return:  w_1 the optimal weight. dimension--(k * sample_num, 1)
    """
    E_or = np.zeros((k * sample_num, 1))
    for i in range(k):
        E_or[sample_num * i: sample_num * (i + 1), 0] = E_list[i][:, 0]

    E = E_or / np.sum(E_or)
    index = np.argsort(E[:, 0])
    E_ascend = E[index, :]

    N = 0
    for idx in range(k*sample_num, 0, -1):
        o = (2 * lam_1 + np.sum(E_ascend[0:idx-1, 0])) / idx - E_ascend[idx-1]

        if o > 0:
            N = idx
            break
    o = (2 * lam_1 + np.sum(E_ascend[1:N, 0])) / N
    w[0:N, 0] =  (o - E_ascend[0:N, 0]) / (2 * lam_1)
    w[N: k * sample_num - 1] = 0

    w_1 = -100 * np.zeros((k * sample_num, 1))
    w_1[index] = w
    return w_1

# E_path = 'E_list.mat'
# w_path = 'w.mat'
# w_1_path = 'w_1.mat'
# E = io.loadmat(E_path)
# w = io.loadmat(w_path)
# w_1 = io.loadmat(w_1_path)
# w_1 = w_1['w_1']
# E = E['E_list']
# E_list = [0, 0 , 0]
# E_list[0] = E[0, 0]
# E_list[1] = E[0, 1]
# E_list[2] = E[0, 2]
# # print(E_list[0].shape)
# w = w['w']
# result = Algorithm_2(sample_num=100, w=w, E_list=E_list, lam_1=1, k=3)
# print(result)
# with open('Algorithm_2_result_python.txt', 'w', encoding='utf-8') as f:
#             f.write('python:\n' + str(result) + '\n')
#             f.write('matlab:\n' + str(w_1) + '\n')

# Eigen_value_path = 'Eigen_Value.mat'
# Eigen_vector_path = 'Eigen_Vector.mat'
# Matrix_path = 'Matrix.mat'
# Eigen_value = io.loadmat(Eigen_value_path)
# Eigen_vector = io.loadmat(Eigen_vector_path)
# Matrix = io.loadmat(Matrix_path)
# Eigen_value = Eigen_value['Eigen_Value']
# Eigen_vector = Eigen_vector['Eigen_Vector']
# Matrix = Matrix['Matrix']
# print('Eigen_value', Eigen_value)
# print('Eigen_vector', Eigen_vector)
# print(Matrix.shape)
# eigen_vector, eigen_value = Find_K_Min_Eigen(Matrix, 50)
# print('eigen_value', eigen_value)
# print('eigen_vector', eigen_vector)
#
# with open('Find_K_min_Eigen.txt', 'w', encoding='utf-8') as f:
#     f.write('Python: \n' + ' eigen_value: '+ str(eigen_value) + '\n')
#     f.write('Matlab: \n' + ' eigen_value: '+ str(Eigen_value) + '\n')
#     f.write('Python: \n' + ' eigen_vector: ' + str(eigen_vector) + '\n')
#     f.write('Matlab: \n' + ' Eigen_vector: ' + str(Eigen_vector) + '\n')