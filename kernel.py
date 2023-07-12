# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 00:43:33 2023

@author: Adil
"""
import numpy as np

def k_x(x_i,x_j,l=1):
    k = (1 + np.sqrt(5) * np.abs(x_i - x_j) / l + 5 / 3 / (l**2) * ((x_i -x_j)**2)) * np.exp(- np.sqrt(5) / l * np.abs(x_i - x_j))
    return k

def k_t(t_i,t_j,l=1):
    k = (1 + np.sqrt(3) / l * np.abs(t_i - t_j)) * np.exp(-np.sqrt(3) / l * np.abs(t_i - t_j))
    return k
    
def k_00(x_i,x_j,t_i,t_j, l_x = 1, l_t = 1):
    k = k_x(x_i,x_j,l_x) * k_t(t_i,t_j,l_t)
    return k

def k_10(x_i,x_j,t_i,t_j, l_x = 1,l_t = 1, a = 1):
    k = (-3 / (l_t**2) * (t_i - t_j) * np.exp(-np.sqrt(3) / l_t * np.abs(t_i - t_j)) * k_x(x_i,x_j,l_x)) - (a * k_t(t_i,t_j,l_t)*(-5 / 3 / (l_x**2) * np.exp(-np.sqrt(5) / l_x * np.abs(x_i - x_j)) * (1 + np.sqrt(5) / l_x * np.abs(x_i -x_j) - 5 / (l_x**2) * (x_i -x_j)**2)))
    return k

def k_11(x_i,x_j,t_i,t_j, l_x = 1,l_t = 1, a = 1):
    k = k_x(x_i,x_j,l_x) * 3 / (l_t**2) * np.exp(-np.sqrt(3) / l_t * np.abs(t_i -t_j)) * (1 - np.sqrt(3) / l_t * np.abs(t_i - t_j)) + a**2 * k_t(t_i,t_j,l_t) * (-25) / 3 / (l_x**4) * np.exp(-np.sqrt(5) /l_x * np.abs(x_i -x_j)) * (-3 + 5 * np.sqrt(5) / l_x * np.abs(x_i - x_j) - 5 / (l_x**2) * (x_i - x_j)**2)
    return k

def kall(x_i,x_j,t_i,t_j,d_i,d_j,l_x=1,l_t=1,a=1):
    if d_i == 0 and d_j ==0:
        return k_00(x_i,x_j,t_i,t_j,l_x,l_t)
    elif d_i == 1 and d_j == 0:
        return k_10(x_i,x_j,t_i,t_j,l_x,l_t,a)
    elif d_i == 0 and d_j ==1:
        return k_10(x_j,x_i,t_j,t_i,l_x,l_t,a)
    else:
        return k_11(x_i,x_j,t_i,t_j,l_x,l_t,a)
        