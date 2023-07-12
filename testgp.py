# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

def covmatrix(x,y):
    lenx = len(x)
    leny = len(y)
    A = np.zeros((lenx,leny))
    for i in range(lenx):
        for j in range(leny):
            A[i,j] = np.exp(-((x[i]-y[j])**2)*200)
 #           A[i,j] = (1 + np.sqrt(3) * 20 * np.abs(x[i] -y[j])) * np.exp(-np.sqrt(3) * 20 * np.abs(x[i] - y[j]))
    return A

x = np.linspace(0, 1,1000)
xt = np.array([0.2105,0.4106,0.5705,0.6207,0.65,0.7596,0.8545,0.9697])
yt = np.array([0.3, 0.32, 0.31,1.93,1.85 ,1.64, 0.32, 0.3])
postmu = (covmatrix(x, xt) @ np.linalg.inv(covmatrix(xt, xt) + 0.02 * np.identity(len(xt))) @ (yt ))
postcov = covmatrix(x, x) - covmatrix(x, xt) @ np.linalg.inv(covmatrix(xt,xt) + 0.02 * np.identity(len(xt))) @ covmatrix(xt, x)
s = np.random.normal(0,1,1000)
#print(postcov)
#A = covmatrix(x,x)
#print(A)
#for j in range(30):
#    unig = np.random.normal(0,1,len(x))
#    L = np.linalg.cholesky(postcov + 1e-6 * np.eye(1000))
#    M = np.random.multivariate_normal(postmu, postcov)
#    M = postmu + unig @ L.T
#    plt.plot(x,M) 

plt.fill_between(x, postmu + 2 * np.sqrt(np.diag(postcov)), postmu - 2 * np.sqrt(np.diag(postcov)),alpha = 0.3)
plt.plot(x,postmu)
plt.plot(x,0*x)
plt.scatter(xt, yt)
