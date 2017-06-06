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
FWHM = data[:, 65]
label = np.zeros((FWHM.shape[0]))
label[FWHM > 0.35] = 0.5
label[FWHM > 0.57] = 1
intensity = [0]*len(Co)

ternary_data = np.concatenate(([Co],[Fe],[Zr],[intensity]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','Fe','Zr'), scale=100,
                       sv=True, svpth=save_path, svflnm='Figure7_gray_ternary',
                       cbl='', vmin = 0, vmax = 1, cmap='gray', cb=True, style='h')


ternary_data = np.concatenate(([Co],[Fe],[Zr],[FWHM]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','Fe','Zr'), scale=100,
                       sv=True, svpth=save_path, svflnm='Figure7_FWHM',
                       cbl='FWHM', cmap='viridis', cb=True, style='h')


ternary_data = np.concatenate(([Co],[Fe],[Zr],[label]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','Fe','Zr'), scale=100,
                       sv=True, svpth=save_path, svflnm='Figure7_glass_formation',
                       cbl='glass formation', vmax = 1, vmin = 0, cmap='viridis_r', cb=True, style='h')
