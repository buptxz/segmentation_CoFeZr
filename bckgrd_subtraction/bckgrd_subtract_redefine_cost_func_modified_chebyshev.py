"""
Created on Feb 8, 2017

@author: fangren
"""

import os.path
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize
from numpy.polynomial.chebyshev import chebval

path = 'C:\\Research_FangRen\\Data\\Metallic_glasses_data\\CoZrFe_ternary\\1D\\raw_1D'
spectrum_file = os.path.join(path, 'Sample3_24x24_t30_0001_1D.csv')

spectrum = np.genfromtxt(spectrum_file, delimiter= ',')
Q = spectrum[:, 0][30:-70]
intensity = spectrum[:, 1][30:-70]


def func(x, *params):
    params = params[0]
    A = params[3]
    B = params[4]
    y = chebval(x, params[:3]) + A/x + B*np.exp(x)
    return y

def object_func(*params):
    params = params[0]
    J = 0
    A = params[3]
    B = params[4]
    fit = chebval(Q, params[:3]) + A/Q + B*np.exp(Q)
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
        # else:
        #     if intensity[i] < fit[i]:
        #         J = J + (intensity[i] - fit[i]) ** 6
        #     elif intensity[i] >= fit[i]:
        #         J = J + (intensity[i] - fit[i]) ** 6
    return J


#
# #x0 = [639.05436108,  238.29655869,  173.94522173, -111.77924248,  13.81729277,  0, 0, 0]
# # x0 = [0,0,0,0,0,0,0]
# x0 = [8.31708595e+02, -9.80154977e+01, 8.08373424e+00, -3.89951175e-01, 8.95326501e+01, 5]
x0 = [771, -51, 0.26, 110, 0.15]
bounds = (671, 871), (-151, 49), (-0.26, 1.26), (10, 220), (0.05, 0.25)


result = minimize(object_func, (771, -51, 0.26, 110, 0.15), bounds = bounds)

bckgrd = func(Q, result.x)

# intensity = intensity - bckgrd
# x0_2 = [.1,0,0]
# result = minimize(object_func_2, x0_2)
# bckgrd =  chebval(Q, result.x)

plt.plot(Q, bckgrd, 'o')
plt.plot(Q, intensity)
plt.figure(4)
plt.plot(Q, intensity - bckgrd)
plt.plot(Q, [0]*len(Q), 'r--')