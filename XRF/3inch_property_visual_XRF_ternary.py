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
from scipy import polyfit


plotTernary = imp.load_source("plt_ternary_save", "plotTernary.py")


path = 'C:\\Research_FangRen\\Data\\July2016\\CoZrFe_ternary\\Masterfiles\\low\\ploting\\'

def twoD_visualize(path):
    """
    create three lists for plotting: plate_x, plate_y, ROI1, ROI2, ROI3...
    """
    for filename in glob.glob(os.path.join(path, '*.csv')):
#        if basename(filename)[0] == '1':
            print basename(filename)
            data = np.genfromtxt(filename, delimiter=',', skip_header = 1)
## top and right
#            ROI1 = np.concatenate((data[:,15][882:],data[:,15][:441]))            
#            ROI2 = np.concatenate((data[:,16][882:],data[:,16][:441]))
#            ROI3 = np.concatenate((data[:,17][882:],data[:,17][:441]))
#            ROI4 = np.concatenate((data[:,18][882:],data[:,18][:441]))
#            ROI5 = np.concatenate((data[:,19][882:],data[:,19][:441]))
#            metal1 = np.concatenate((data[:,57][882:],data[:,57][:441]))
#            metal2 = np.concatenate((data[:,58][882:],data[:,58][:441]))
#            metal3 = np.concatenate((data[:,59][882:],data[:,59][:441]))
#            peak_position = np.concatenate((data[:,60][882:],data[:,60][:441]))
#            peak_width = np.concatenate((data[:,61][882:],data[:,61][:441]))    
#            peak_intensity = np.concatenate((data[:,62][882:],data[:,62][:441]))
## top and left
#            ROI1 = np.concatenate((data[:,15][441:882],data[:,15][:441]))
#            ROI2 = np.concatenate((data[:,16][441:882],data[:,16][:441]))
#            ROI3 = np.concatenate((data[:,17][441:882],data[:,17][:441]))
#            ROI4 = np.concatenate((data[:,18][441:882],data[:,18][:441]))
#            ROI5 = np.concatenate((data[:,19][441:882],data[:,19][:441]))
#            metal1 = np.concatenate((data[:,57][441:882],data[:,57][:441]))
#            metal2 = np.concatenate((data[:,58][441:882],data[:,58][:441]))
#            metal3 = np.concatenate((data[:,59][441:882],data[:,59][:441]))
#            peak_position = np.concatenate((data[:,60][441:882],data[:,60][:441]))
#            peak_width = np.concatenate((data[:,61][441:882],data[:,61][:441]))    
#            peak_intensity = np.concatenate((data[:,62][441:882],data[:,62][:441]))
### left and right
#            ROI2 = np.concatenate((data[:,16][882:],data[:,16][441:882]))
#            ROI1 = np.concatenate((data[:,15][882:],data[:,15][441:882]))
#            ROI3 = np.concatenate((data[:,17][882:],data[:,17][441:882]))
#            ROI4 = np.concatenate((data[:,18][882:],data[:,18][441:882]))
#            ROI5 = np.concatenate((data[:,19][882:],data[:,19][441:882]))
#            metal1 = np.concatenate((data[:,57][882:],data[:,57][441:882]))
#            metal2 = np.concatenate((data[:,58][882:],data[:,58][441:882]))
#            metal3 = np.concatenate((data[:,59][882:],data[:,59][441:882]))
#            peak_position = np.concatenate((data[:,60][882:],data[:,60][441:882]))
#            peak_width = np.concatenate((data[:,61][882:],data[:,61][441:882]))    
#            peak_intensity = np.concatenate((data[:,62][882:],data[:,62][441:882]))
# whole ternary
            ROI1 = data[:,15]
            ROI2 = data[:,16]
            ROI3 = data[:,17]
            ROI4 = data[:,18]
            ROI5 = data[:,19]
            ROI6 = data[:,20]
            metal1 = data[:,54]
            metal2 = data[:,55]
            metal3 = data[:,56]
    return ROI1, ROI2, ROI3, ROI4, ROI5, ROI6, metal1, metal2, metal3

                 
ROI1, ROI2, ROI3, ROI4, ROI5, ROI6, metal1, metal2, metal3 = twoD_visualize(path)

plt.figure(1)
plt.plot(metal2, ROI1, 'o')
m,b = polyfit(ROI1, metal2, 1)
plt.plot(ROI1*m, ROI1, 'o')


#plt.figure(2)
#plt.plot(metal1, ROI3, 'o')
#m,b = polyfit(ROI3, metal1, 1) 
#plt.plot(m*ROI3, ROI3, 'o')
#plt.xlim(0, 100)


#ternary_data = np.concatenate(([metal1],[metal2],[metal3],[ROI1]), axis = 0)
#ternary_data = np.transpose(ternary_data)
#
#plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','Fe','Zr'), scale=100,
#                       sv=True, svpth=path, svflnm='ROI1',
#                       cbl='Scale', vmin = 772, vmax = 1211222.0, cmap='jet', cb=True, style='h')
#
#
#ternary_data = np.concatenate(([metal1],[metal2],[metal3],[ROI2]), axis = 0)
#ternary_data = np.transpose(ternary_data)
#
#plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','Fe','Zr'), scale=100,
#                       sv=True, svpth=path, svflnm='ROI2',
#                       cbl='Scale', vmin = 772, vmax = 1051932.0, cmap='jet', cb=True, style='h')
#                       
#ternary_data = np.concatenate(([metal1],[metal2],[metal3],[ROI3]), axis = 0)
#ternary_data = np.transpose(ternary_data)
#
#plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','Fe','Zr'), scale=100,
#                       sv=True, svpth=path, svflnm='ROI3',
#                       cbl='Scale', vmin = 772, vmax = 150579.0, cmap='jet', cb=True, style='h')
#                       
#ternary_data = np.concatenate(([metal1],[metal2],[metal3],[ROI4]), axis = 0)
#ternary_data = np.transpose(ternary_data)
#
#plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','Fe','Zr'), scale=100,
#                       sv=True, svpth=path, svflnm='ROI4',
#                       cbl='Scale', vmin = 772, vmax = 11192.0, cmap='jet', cb=True, style='h')
#                       
#ternary_data = np.concatenate(([metal1],[metal2],[metal3],[ROI5]), axis = 0)
#ternary_data = np.transpose(ternary_data)
#
#plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','Fe','Zr'), scale=100,
#                       sv=True, svpth=path, svflnm='ROI5',
#                       cbl='Scale', vmin = 772, vmax = 4592.0, cmap='jet', cb=True, style='h')
#                       
#ternary_data = np.concatenate(([metal1],[metal2],[metal3],[ROI6]), axis = 0)
#ternary_data = np.transpose(ternary_data)
#
#plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','Fe','Zr'), scale=100,
#                       sv=True, svpth=path, svflnm='ROI6',
#                       cbl='Scale', vmin = 772, vmax = 4972.0, cmap='jet', cb=True, style='h')
#
#
#
#plt.close("all")

