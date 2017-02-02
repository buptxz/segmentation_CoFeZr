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
#        if basename(filename)[0] == '1':
            print basename(filename)
            data = np.genfromtxt(filename, delimiter=',', skip_header = 1)
            Co = data[:,54]
            Fe = data[:,55]
            Zr = data[:,56]
            peak_position = data[:,57]
            peak_width = data[:,58] 
            peak_intensity = data[:,59]
    return Co, Fe, Zr, peak_position, peak_width, peak_intensity
                 
Co, Fe, Zr, peak_position, peak_width, peak_intensity = twoD_visualize(path)


ternary_data = np.concatenate(([Co],[Fe],[Zr],[peak_width]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','Fe','Zr'), scale=100,
                       sv=True, svpth=path, svflnm='peak_width_ternary',
                       cbl='Scale', vmin = 0.028, vmax = 0.458, cmap='jet_r', cb=True, style='h')

labels = []
for pw in peak_width:
    if pw < 0.18:
        label = 3
    elif pw > 0.35:
        label = 1
    else:
        label = 2
    labels.append(label)

ternary_data = np.concatenate(([Co],[Fe],[Zr],[labels]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','Fe','Zr'), scale=100,
                       sv=True, svpth=path, svflnm='glass_or_crystal',
                       cbl='Scale', vmin = 0.2, vmax = 3.2, cmap='jet', cb=True, style='h')



ternary_data = np.concatenate(([Co],[Fe],[Zr],[peak_intensity]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','Fe','Zr'), scale=100,
                       sv=True, svpth=path, svflnm='peak_intensity_ternary',
                       cbl='Scale', vmin=137, vmax=5630, cmap='jet', cb=True, style='h')
                       

ternary_data = np.concatenate(([Co],[Fe],[Zr],[peak_position]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','Fe','Zr'), scale=100,
                       sv=True, svpth=path, svflnm='peak_position_ternary',
                       cbl='Scale', vmin=2.30, vmax=3.15, cmap='jet', cb=True, style='h')

##
#ternary_data = np.concatenate(([Co],[Fe],[Zr],[peak_num]), axis = 0)
#ternary_data = np.transpose(ternary_data)
#
#plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','Fe','Zr'), scale=100,
#                       sv=True, svpth=path, svflnm='peak_num',
#                       cbl='Scale', vmin = 1, vmax = 14,  cmap='jet', cb=True, style='h')


plt.close("all")

