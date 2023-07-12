# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 21:28:11 2023

@author: Adil
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 100)
y = (1 + np.sqrt(3) * np.abs(x - 0.4)) * (np.exp(-np.sqrt(3) * np.abs(x - 0.4)))
fdy = np.gradient(y, x)
ady = -3 * np.exp(-np.sqrt(3) * np.abs(x - 0.4)) * (x - 0.4)

x_1 = np.linspace(0, 1, 100)
A = np.zeros((100,100))
dA = np.zeros((100,100))
for i in range(len(x)):
    for j in range(len(x_1)):
        A[i,j] = (1 + np.sqrt(3) * np.abs(x[i] - x_1[j])) * (np.exp(-np.sqrt(3) * np.abs(x[i] - x_1[j])))
        dA[i,j] = 3 * (1 - np.sqrt(3) * np.abs(x[i] - x_1[j])) * (np.exp(-np.sqrt(3) * np.abs(x[i] - x_1[j])))
fddydx = np.gradient(np.gradient(A, 0.01,axis = 0), 0.01,axis = 1)
fig, ax1 = plt.subplots()

plt.grid(linestyle='--', linewidth=0.5)
color = 'tab:red'
ax1.set_xlabel('time (s)')
ax1.set_ylabel('function', color=color)
ax1.plot(x, y, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('derivative', color=color)  # we already handled the x-label with ax1
ax2.plot(x, fdy, color=color, linestyle='--', linewidth = 2)
ax2.plot(x,ady, color = 'tab:green')
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()

fig2, ax3 = plt.subplots()
imA = ax3.imshow(A)
plt.colorbar(imA)

fig3,ax4 = plt.subplots()
imdA = ax4.imshow(dA)
plt.colorbar(imdA)

fig4,ax5 = plt.subplots()
imdiff = ax5.imshow(fddydx)
plt.colorbar(imdiff)