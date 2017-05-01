"""
Created on Feb 8, 2017

@author: fangren
"""

import os.path
import matplotlib.pyplot as plt
import numpy as np
import copy
from numpy.polynomial import chebyshev


path = 'C:\\Research_FangRen\\Data\\Metallic_glasses_data\\CoZrFe_ternary\\1D\\raw_1D'
spectrum_file = os.path.join(path, 'Sample3_24x24_t30_0001_1D.csv')


spectrum = np.genfromtxt(spectrum_file, delimiter= ',')
Q = spectrum[:, 0][30:-70]
intensity = spectrum[:, 1][30:-70]

Q_bckgrd = []
intensity_bckgrd = []

for i in np.arange(0, len(Q), 40):
    Q_bckgrd.append(Q[i])
    intensity_bckgrd.append(intensity[i])

param = chebyshev.chebfit(Q_bckgrd, intensity_bckgrd, 4)
bckgrd = chebyshev.chebval(Q_bckgrd, param)


for j in range(30):
    for i in range(len(bckgrd)-2):
        print i
        left_neighbor = bckgrd[i]
        middle = bckgrd[i+1]
        right_neighbor = bckgrd[i+2]
        if middle > (left_neighbor+right_neighbor)/2:
            bckgrd[i+1] = (left_neighbor+right_neighbor)/2


plt.plot(Q_bckgrd, bckgrd, 'o')
plt.plot(Q_bckgrd, intensity_bckgrd, 'o')
plt.plot(Q, intensity)
# plt.figure(4)
# plt.plot(Q, intensity - bckgrd)