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


plotTernary = imp.load_source("plt_ternary_save", "plotTernary.py")


path = 'C:\\Research_FangRen\Data\\July2016\\CoZrFe_ternary\\Masterfiles\\high\\ploting\\'


def twoD_visualize(path):
    """
    create three lists for plotting: plate_x, plate_y, ROI1, ROI2, ROI3...
    """
    for filename in glob.glob(os.path.join(path, '*.csv')):
        # if basename(filename)[0] == 'A':
            print basename(filename)
            data = np.genfromtxt(filename, delimiter=',', skip_header = 1)
            Co = data[:,54]
            Fe = data[:,55]
            Zr = data[:,56]
            peak_num = data[:,60]
            crystallinity = data[:,51] 
            texture = data[:,53]
            distance = data[:, 61]
            SNR = data[:, 62]
            
    return Co, Fe, Zr, peak_num, crystallinity, texture, distance, SNR
                 
Co, Fe, Zr, peak_num, crystallinity, texture, distance, SNR = twoD_visualize(path)


#ternary_data = np.concatenate(([Co],[Fe],[Zr],[peak_num]), axis = 0)
#ternary_data = np.transpose(ternary_data)
#
#plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','Fe','Zr'), scale=100,
#                       sv=True, svpth=path, svflnm='peak_num_ternary',
#                       cbl='Scale', vmin = 0, vmax = 6, cmap='jet', cb=True, style='h')
#
#
#
#ternary_data = np.concatenate(([Co],[Fe],[Zr],[np.log(crystallinity)]), axis = 0)
#ternary_data = np.transpose(ternary_data)
#
#plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','Fe','Zr'), scale=100,
#                       sv=True, svpth=path, svflnm='crystallinity',
#                       cbl='Scale', vmin=0.2, vmax=1.4, cmap='jet', cb=True, style='h')
#                       
#
#ternary_data = np.concatenate(([Co],[Fe],[Zr],[np.log(texture)]), axis = 0)
#ternary_data = np.transpose(ternary_data)
#
#plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','Fe','Zr'), scale=100,
#                       sv=True, svpth=path, svflnm='texture',
#                       cbl='Scale', vmin=-11.1, vmax=-10.3, cmap='jet', cb=True, style='h')

#
ternary_data = np.concatenate(([Co],[Fe],[Zr],[SNR]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','Fe','Zr'), scale=100,
                       sv=False, svpth=path, svflnm='SNR',
                       cbl='Scale', cmap='jet', cb=True, style='h')


# plt.close("all")

