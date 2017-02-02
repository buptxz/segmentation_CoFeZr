# -*- coding: utf-8 -*-
"""
Created on Wed July 13 2016

@author: fangren

Implement from paper:
"Power-law scaling and fractal nature of medium-range order in metallic glasses"
D. Ma, et al
Nature Materials
"""

import numpy as np
import matplotlib.pyplot as plt
import glob
import os
from os.path import basename
import imp

plotTernary = imp.load_source("plt_ternary_save", "plotTernary.py")

# the master csv file that has chemical compositions of Co, V, Zr and peak positions of XRD spectra
path = 'C:\\Research_FangRen\\Publications\\Combinatorial Search for Metallic Glasses in Co-V-Zr ternary systems\\theory\\'


def twoD_visualize(path):
    """
    Extract data from four columns: chemical compositions and peak_positions from the master file in the path
    """
    for filename in glob.glob(os.path.join(path, '*.csv')):
#        if basename(filename)[0] == '1':
            print basename(filename)
            data = np.genfromtxt(filename, delimiter=',', skip_header = 1)
            Co = data[:,54]
            V = data[:,55]
            Zr = data[:,56]
            peak_position = data[:,57]
    return Co, V, Zr, peak_position
             
           
Co, V, Zr, peak_position = twoD_visualize(path)


Co_c = Co/100.0
V_c = V/100.0
Zr_c = Zr/100.0

# calculatin is shown in a separate word file
Co_volume = 11.025
V_volume = 14.74
Zr_volume = 24.66


atomic_volume = Co_c * Co_volume + V_c * V_volume + Zr_c * Zr_volume

scale = peak_position * atomic_volume ** 0.433

#ternary_data = np.concatenate(([Co],[V],[Zr],[atomic_volume]), axis = 0)
#ternary_data = np.transpose(ternary_data)
#
#plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
#                       sv=True, svpth=path, svflnm='atomic volume',
#                       cbl='Scale', cmap='jet_r', cb=True, style='h')
#
#
#ternary_data = np.concatenate(([Co],[V],[Zr],[peak_position]), axis = 0)
#ternary_data = np.transpose(ternary_data)
#
#plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
#                       sv=True, svpth=path, svflnm='peak position',
#                       cbl='Scale', cmap='jet_r', cb=True, style='h')
#

ternary_data = np.concatenate(([Co],[V],[Zr],[scale]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
                       sv=True, svpth=path, svflnm='power_scaling',
                       cbl='Scale', cmap='jet_r', cb=True, style='h')
                       
quasicrystals = np.abs(scale - 9.3) < 0.2           
            
ternary_data = np.concatenate(([Co],[V],[Zr],[quasicrystals]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
                       sv=True, svpth=path, svflnm='quasicrystals',
                       cbl='Scale', cmap='jet_r', cb=True, style='h')                

plt.close('all')