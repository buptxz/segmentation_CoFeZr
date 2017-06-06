# -*- coding: utf-8 -*-
"""
Created on Wed July 13 2016

@author: fangren

contributed by T Williams
"""


import numpy as np
import matplotlib.pyplot as plt
import glob
import os
from os.path import basename
import imp
import scipy
from scipy import interpolate


plotTernary = imp.load_source("plt_ternary_save", "plotTernary.py")


path = '..\\..\\data\\Masterfiles\\'
save_path = '..\\..\\figures\\'

basename1 = 'Sample1_master_metadata.csv'
basename2 = 'Sample3_master_metadata.csv'
basename3 = 'Sample16_master_metadata.csv'

filename1 = path + basename1
filename2 = path + basename2
filename3 = path + basename3

data1 = np.genfromtxt(filename1, delimiter=',', skip_header = 1)
data2 = np.genfromtxt(filename2, delimiter=',', skip_header = 1)
data3 = np.genfromtxt(filename3, delimiter=',', skip_header = 1)

data = np.concatenate((data1[:, :69], data2[:, :69], data3[:, :69]))
# data = data1[:50, :69]
ROI = data[:, 15]
data = data[ROI > 20000]

Co = data[:,61]*100
Fe = data[:,62]*100
Zr = data[:,63]*100

peak_number = data[:, 55]
nearest_neighbor = data[:, 57]
texture_sum = data[:, 53]
crystallinity = data[:, 51]
peak_position = data[:,64]
peak_width = data[:,65]
peak_intensity = data[:,66]
nearest_neighbor_2d = data[:, 67]




ternary_data = np.concatenate(([Co],[Fe],[Zr],[np.log(nearest_neighbor)]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','Fe','Zr'), scale=100,
                       sv=True, svpth=save_path, svflnm='Figure3(a)_nearest_neighbor_1d',
                       cbl='Nearest-neighbor distances(1D)', vmin = -10.8, vmax = np.nanmax(np.log(nearest_neighbor)), cmap='viridis', cb=True, style='h')


ternary_data = np.concatenate(([Co],[Fe],[Zr],[np.log(nearest_neighbor_2d)]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','Fe','Zr'), scale=100,
                       sv=True, svpth=save_path, svflnm='Figure3(b)_nearest_neighbor_2d',
                       cbl='Nearest-neighbor distances (2D)', vmin = -8.7, vmax = np.nanmax(np.log(nearest_neighbor_2d)), cmap='viridis', cb=True, style='h')


plt.figure(3, figsize = (10,8))
plt.subplot(211)
#plt.hist(np.log(nearest_neighbor), bins = 100, range = (np.nanmin(np.log(nearest_neighbor)), np.nanmax(np.log(nearest_neighbor))), label = '1D spectra')
#plt.hist(np.log(nearest_neighbor), bins = 100, range = (-10.8, -4.7), label = '1D spectra')
plt.hist(np.log(nearest_neighbor), bins = 100, range = (-10.8, np.nanmax(np.log(nearest_neighbor))), label = '1D spectra')
plt.legend()
plt.subplot(212)
#plt.hist(np.log(nearest_neighbor_2d), bins = 100, range = (np.nanmin(np.log(nearest_neighbor_2d)), np.nanmax(np.log(nearest_neighbor_2d))), label = '2D images', color = 'orange')
#plt.hist(np.log(nearest_neighbor_2d), bins = 100, range = (-8.7, -4.8), label = '2D images', color = 'orange')
plt.hist(np.log(nearest_neighbor_2d), bins = 100, range = (-8.7, np.nanmax(np.log(nearest_neighbor_2d))), label = '2D images', color = 'orange')
plt.legend()
plt.savefig(save_path + 'Figure3_nearest_neighbor_hist', dpi = 600)