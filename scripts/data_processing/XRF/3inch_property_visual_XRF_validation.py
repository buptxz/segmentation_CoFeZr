## -*- coding: utf-8 -*-
#"""
#Created on Wed July 13 2016
#
#@author: fangren
#"""


import numpy as np
import matplotlib.pyplot as plt
import glob
import os
from os.path import basename
import imp
from scipy.stats import linregress


plotTernary = imp.load_source("plt_ternary_save", "plotTernary.py")

path = 'C:\\Research_FangRen\\XRF\\'

filename = 'C:\Research_FangRen\XRF\mca_files\master_files_XRF\\CLEANED_Sample10_master_metadata_low.csv'

data = np.genfromtxt(filename, delimiter=',', skip_header = 1)
plate_x = data[:,1]
plate_y = data[:,2]
ROI2 = data[:, 16]
Co = data[:,57]*100
V = data[:,58]*100
Zr = data[:,59]*100
V_alpha1 = data[:,63]
V_alpha2 = data[:,64]
V_beta = data[:,65]
Co_alpha1 = data[:,66]
Co_alpha2 = data[:,67]
Co_beta = data[:,68]

plt.figure(1)
plt.plot(Co_alpha1, Co, 'o')
# # plt.plot(Co_alpha1, Co_alpha1* slope + intercept)
# #
plt.figure(2)
plt.plot(V_alpha1, V, 'o')
# # plt.plot(V_alpha1, V_alpha1 * slope + intercept)

# plt.figure(1)
# plt.plot(Co_alpha1/V_alpha1, Co/V, 'o')
# plt.plot(Co_alpha1, Co_alpha1* slope + intercept)

# ternary_data = np.concatenate(([Co],[V],[Zr],[Co_alpha1]), axis = 0)
# ternary_data = np.transpose(ternary_data)
#
# plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
#                        sv=False, svpth=path, svflnm='Co_alpha1',
#                        cbl='Scale', cmap='jet', cb=True, style='h')

ternary_data = np.concatenate(([Co],[V],[Zr],[V_alpha1]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
                       sv=False, svpth=path, svflnm='V_alpha1',
                       cbl='Scale', cmap='jet', cb=True, style='h')
#
#

