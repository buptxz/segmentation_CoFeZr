# -*- coding: utf-8 -*-
"""
Created on Feb 3, 2017

@author: fangren
"""

import os.path
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import splev, splrep
import copy

path = 'C:\\Research_FangRen\\Data\\Metallic_glasses_data\\CoZrFe_ternary\\1D\\raw_1D'

silicon_file = os.path.join(path, 'Sample1_24x24_t30_0233_1D.csv')
spectrum_file = os.path.join(path, 'Sample1_24x24_t30_0001_1D.csv')

silicon = np.genfromtxt(silicon_file, delimiter=',')
spectrum = np.genfromtxt(spectrum_file, delimiter= ',')
Q = silicon[:, 0][30:-70]
bckgrd = silicon[: ,1][30:-70]
intensity = spectrum[:, 1][30:-70]

bckgrd = copy.copy(intensity)

first_points = np.array([intensity[:200]])

for i in range(100):
    # print first_points, bckgrd[0]
    param = np.polyfit(Q, np.append(first_points, bckgrd[200:]), 3)
    bckgrd_new = np.matrix([param]) * np.matrix([Q**3, Q**2, Q, np.ones(Q.shape)])
    bckgrd = np.minimum(bckgrd, bckgrd_new)
    bckgrd = np.array(bckgrd)[0]

plt.figure(1)
plt.plot(Q, bckgrd)
plt.plot(Q, intensity)
