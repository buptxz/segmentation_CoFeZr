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


path = 'C:\\Research_FangRen\\Data\\July2016\\CoZrFe_ternary\\Masterfiles\\high\\ploting\\'

def twoD_visualize(path):
    """
    create three lists for plotting: plate_x, plate_y, peak number...
    """
    for filename in glob.glob(os.path.join(path, '*.csv')):
#        if basename(filename)[0] == '1':
            print basename(filename)
            data = np.genfromtxt(filename, delimiter=',', skip_header = 1)
            plate_x = data[:,1][:439]
            plate_y = data[:,2][:439]
            peak_num = data[:,60][:439]
            crystallinity = data[:,51][:439]
            texture = data[:,53][:439]
    return plate_x, plate_y, peak_num, crystallinity, texture
                 
plate_x, plate_y, peak_num, crystallinity, texture = twoD_visualize(path)

area = 380


plt.figure(5, figsize = (12, 9))
plt.title('crystallinity analysis')
plt.scatter(plate_y, plate_x, c = np.log(crystallinity), s = area, marker = 's')
plt.xlim((-36, 36))
plt.ylim((-36, 36))
plt.colorbar()
plt.xlabel('plate_y')
plt.ylabel('plate_x(flat)')
plt.clim((0.2, 1.4))
plt.savefig(path+'crystallinity analysis')

plt.figure(6, figsize = (12, 9))
plt.title('texture analysis')
plt.scatter(plate_y, plate_x, c = np.log(texture), s = area, marker = 's')
plt.xlim((-36, 36))
plt.ylim((-36, 36))
plt.colorbar()
plt.xlabel('plate_y')
plt.ylabel('plate_x(flat)')
plt.clim((-11.1, -10.3))
plt.savefig(path+'texture analysis')

plt.figure(7, figsize = (12, 9))
plt.title('peak number')
plt.scatter(plate_y, plate_x, c = peak_num, s = area, marker = 's')
plt.xlim((-36, 36))
plt.ylim((-36, 36))
plt.colorbar()
plt.xlabel('plate_y')
plt.ylabel('plate_x(flat)')
plt.clim((1, 8))
plt.savefig(path+'peak_number')

plt.close("all")

