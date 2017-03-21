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


# path = 'C:\\Research_FangRen\\Data\\July2016\\CoZrFe_ternary\\Masterfiles\\high\\ploting\\'
path = 'C:\\Research_FangRen\\Publications\\on_the_fly_paper\\Sample_data\\'

def twoD_visualize(path):
    """
    create three lists for plotting: plate_x, plate_y, ROI1, ROI2, ROI3...
    """
    for filename in glob.glob(os.path.join(path, '*.csv')):
        if basename(filename)[0] == '2':
            print basename(filename)
            data = np.genfromtxt(filename, delimiter=',', skip_header = 1)
            plate_x = data[:,1]
            plate_y = data[:,2]
            ROI1 = data[:,15]
            ROI2 = data[:,16]
            ROI3 = data[:,17]
            ROI4 = data[:,18]
            ROI5 = data[:,19]
            ROI6 = data[:,20]
    return plate_x, plate_y, ROI1, ROI2, ROI3, ROI4, ROI5, ROI6

                 
plate_x, plate_y, ROI1, ROI2, ROI3, ROI4, ROI5, ROI6 = twoD_visualize(path)

# area = 460
area = 300


# plt.figure(1, figsize = (12, 9))
# plt.title('ROI1')
# plt.scatter(plate_y, plate_x, c = ROI1, s = area, marker = 's')
# plt.colorbar()
# plt.xlim((-36, 36))
# plt.ylim((-36, 36))
# plt.xlabel('plate_y')
# plt.ylabel('plate_x(flat)')
# plt.savefig(path+'ROI1.png')
#
# plt.figure(2, figsize = (12, 9))
# plt.title('ROI2')
# plt.scatter(plate_y, plate_x, c = ROI2, s = area, marker = 's')
# plt.colorbar()
# plt.xlim((-36, 36))
# plt.ylim((-36, 36))
# plt.xlabel('plate_y')
# plt.ylabel('plate_x(flat)')
# plt.savefig(path+'ROI2.png')
#
# plt.figure(3, figsize = (12, 9))
# plt.title('ROI3')
# plt.scatter(plate_y, plate_x, c = ROI3, s = area, marker = 's')
# plt.colorbar()
# plt.xlim((-36, 36))
# plt.ylim((-36, 36))
# plt.xlabel('plate_y')
# plt.ylabel('plate_x(flat)')
# plt.savefig(path+'ROI3.png')
#
# plt.figure(4, figsize = (12, 9))
# plt.title('ROI4')
# plt.scatter(plate_y, plate_x, c = ROI4, s = area, marker = 's')
# plt.colorbar()
# plt.xlim((-36, 36))
# plt.ylim((-36, 36))
# plt.xlabel('plate_y')
# plt.ylabel('plate_x(flat)')
# plt.savefig(path+'ROI4.png')

plt.figure(5, figsize = (12, 9))
plt.title('XRF')
plt.scatter(plate_y, plate_x, c = ROI5, s = area, marker = 's')
plt.colorbar()
plt.xlim((-44, 44))
plt.ylim((-44, 44))
plt.xlabel('x')
plt.ylabel('y')
plt.savefig(path+'ROI5.png', dpi = 600)

# plt.figure(6, figsize = (12, 9))
# plt.title('ROI6')
# plt.scatter(plate_y, plate_x, c = ROI6, s = area, marker = 's')
# plt.colorbar()
# plt.xlim((-36, 36))
# plt.ylim((-36, 36))
# plt.xlabel('plate_y')
# plt.ylabel('plate_x(flat)')
# plt.savefig(path+'ROI6.png')

plt.close("all")

