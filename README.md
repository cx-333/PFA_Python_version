# PFA_Python_version
Python code for realizing the algorithm of the paper 'Pattern fusion analysis by adaptive alignment of multiple heterogeneous omics data'. 


# 0 Introduction
*In the paper 'Pattern fusion analysis by adaptive alignment of multiple heterogeneous omics data', the implementation of the paper's algorithm is based on MATLAB. For those who are not well in MATLAB language, I transform the algorithm of MATLAB version to corresponding Python version.* The PFA algorithm of Python version is a little different from its corresponding MATLAB version. 

# 1 Different points
 * The original PFA algorithm of MATLAB version include PCA step, while in its Python version not existing. Hence, you can use a specific dimensionality reduction algorithm before call for this program or  directly using this program.
 * The main program of the algorithm is in Algorithm 4. You can directly use Algorithm 4 to achieve PFA algorithm without PCA dimensionality reduction.

# 2 Requirements
The PFA algorithm of Python version is based on *Numpy* package, so before using this programming. Your computer should been have:
 * numpy 
 * python >= 3.x
 
 # 3 Usage
  * Input variable description
     * k: the number of data type
     * d_num: d_num = np.min(xList[0].shape[0], xList[1].shape[0], ..., xList[k-1].shape[0])
     * lam_1: tuning parameter, defalut lam_1 = 1
     * iter_num: the number of iterating. default iter_num = 1000
     * sample_num: the number of sample
     * xList: store input data, the length of xList is k. the format of xList[i] ($i\in [0, k-1]$): a $m\times n$ matrix, which m denote gene name and n denote sample name.
  * Output description
     * Y: the result of output. $Y\times Y^{T} = 1$. a $d_{num}\times sample_{num}$ matrix.
     * w: the weight of every sample. $w >= 0$.
     * L_list:a list, the length of it is k. the format of L_list[i] ($i\in [0, k-1]$):a $d_m\times xList[i].shape[0]$ matrix.
 After clone this repository, you can simulate following example to use this algorithm:
 ```python
 from Algorithm_4 import Algorithm_4
 import numpy as np
  
 k = 3
 lam_1 = 1
 iter_num = 1000
 sample_num = 100
 xList = []
 for i in range(k):
    xList.append(0)
 xList[0] = np.random.random((36, sample_num))
 xList[1] = np.random.random((40, sample_num))
 xList[2] = np.random.random((50, sample_num))
 
 Y, w, L_list = Algorithm_4(xList, sample_num, iter_num, lam_1, d_num, k)
 
 print('#'*200)
 print(np.diag(Y.dot(Y.T)))
 print('#'*200)
 print(np.sum(w >= 0))
 print('#'*200)
 print(L_list)
 
 ```
 
 
 
