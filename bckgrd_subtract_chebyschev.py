"""
Created on Feb 8, 2017

@author: fangren
"""

import os.path
import matplotlib.pyplot as plt
import numpy as np
import copy
from numpy.polynomial import chebyshev

def replace_head_tail(intensity, bckgrd):
    bckgrd_new = np.concatenate((intensity[:130], bckgrd[130:600], intensity[600:]))
    return bckgrd_new

def head_tail(Q, intensity):
    Q = np.concatenate((Q[:130], Q[600:]))
    intensity = np.concatenate((intensity[:130], intensity[600:]))
    return Q, intensity

path = 'C:\\Research_FangRen\\Data\\Metallic_glasses_data\\CoZrFe_ternary\\1D\\raw_1D'
spectrum_file = os.path.join(path, 'Sample3_24x24_t30_0001_1D.csv')
silicon_file = os.path.join(path, 'Sample1_24x24_t30_0233_1D.csv')

spectrum = np.genfromtxt(spectrum_file, delimiter= ',')
silicon = np.genfromtxt(silicon_file, delimiter= ',')
Q = spectrum[:, 0][30:-70]
intensity = spectrum[:, 1][30:-70]
# silicon_bckgrd = silicon[:, 1][30:-70]
#intensity = intensity - silicon_bckgrd
# intensity[intensity>np.mean(intensity)] = np.mean(intensity)

bckgrd = copy.copy(intensity)

# param = chebyshev.chebfit(Q, intensity, 4)
# bckgrd = chebyshev.chebval(Q, param)


    # print first_points, bckgrd[0]
param = chebyshev.chebfit(head_tail(Q, intensity), 4)
bckgrd = chebyshev.chebval(Q, param)
    # plt.figure(2)
    # plt.plot(Q, bckgrd_new)
    bckgrd = np.minimum(bckgrd, bckgrd_new)
    # plt.figure(3)
    # plt.plot(Q, bckgrd)
    bckgrd = replace_head_tail(intensity, bckgrd)
    # plt.figure(4)
    # plt.plot(Q, bckgrd)
#
plt.figure(5)
plt.plot(Q, bckgrd)
plt.plot(Q, intensity)
plt.figure(4)
plt.plot(Q, intensity - bckgrd)