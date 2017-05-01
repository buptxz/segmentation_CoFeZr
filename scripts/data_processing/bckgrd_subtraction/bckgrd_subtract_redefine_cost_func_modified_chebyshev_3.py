"""
Created on Feb 8, 2017

@author: fangren
"""

import os.path
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize
from numpy.polynomial.polynomial import polyfit, polyval

path = 'C:\\Research_FangRen\\Data\\Metallic_glasses_data\\CoZrFe_ternary\\1D\\raw_1D'
spectrum_file = os.path.join(path, 'Sample3_24x24_t30_0001_1D_cropped.csv')
spectrum_file_2 = os.path.join(path, 'Sample3_24x24_t30_0002_1D.csv')

spectrum = np.genfromtxt(spectrum_file, delimiter= ',')
Q = spectrum[:, 0][30:-70]
intensity = spectrum[:, 1][30:-70]

spectrum_2 = np.genfromtxt(spectrum_file_2, delimiter= ',')
Q_full = spectrum_2[:, 0][30:-70]

result = polyfit(Q, intensity, 4)

bckgrd = polyval(Q_full, result)
plt.plot(Q, intensity)
plt.plot(Q_full, bckgrd)