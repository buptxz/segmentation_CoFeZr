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
spectrum_file = os.path.join(path, 'Sample3_24x24_t30_0400_1D.csv')

spectrum = np.genfromtxt(spectrum_file, delimiter= ',')
Q = spectrum[:, 0][30:-70]
intensity = spectrum[:, 1][30:-70]

def object_func(*params):
    params = params[0]
    J = 0
    fit = polyval(Q, params)
    for i in range(len(intensity)):
        if i < 150:
            if intensity[i] < fit[i]:
                J = J + (intensity[i]-fit[i])**6
            elif intensity[i] >= fit[i]:
                J = J + (intensity[i]-fit[i])**6
        elif i >= 100:
            if intensity[i] < fit[i]:
                J = J + (intensity[i] - fit[i]) ** 6
            elif intensity[i] >= fit[i]:
                J = J + (intensity[i] - fit[i]) ** 2
    return J



x0 = [1417.64221453, -694.54713297, 284.95391128, -55.25140044, 3.82028186]

limit = ((1000, 2000), (-704, -680), (275, 295), (-60, -50), (3.72, 3.92))

result = minimize(object_func, x0, bounds = limit)

bckgrd = polyval(Q, result.x)

plt.plot(Q, bckgrd, 'o')
plt.plot(Q, intensity)
plt.figure(4)
plt.plot(Q, intensity - bckgrd)
plt.plot(Q, [0]*len(Q), 'r--')