"""
Created on Feb 8, 2017

@author: fangren
"""

import os.path
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize


path = 'C:\\Research_FangRen\\Data\\Metallic_glasses_data\\CoZrFe_ternary\\1D\\raw_1D'
spectrum_file = os.path.join(path, 'Sample3_24x24_t30_0001_1D.csv')

spectrum = np.genfromtxt(spectrum_file, delimiter= ',')
Q = spectrum[:, 0][30:-70]
intensity = spectrum[:, 1][30:-70]


def func(x, *params):
    params = params[0]
    A = params[0]
    B = params[1]
    C = params[2]
    D = params[3]
    E = params[4]
    #y = A + B/x + C*x + D * (x**2) + E * (x**3)
    F = params[5]
    y = A + B/(x**2) + C*x + D * (x**2) + E * (x**3)
    return y

def object_func(*params):
    params = params[0]
    J = 0
    A = params[0]
    B = params[1]
    C = params[2]
    D = params[3]
    E = params[4]
    #fit = A + B/Q + C*Q + D * (Q**2) + E * (Q**3)
    F = params[5]
    fit = A + B/(Q**2) + C*Q + D * (Q**2) + E * (Q**3)
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

Q_bckgrd = []
intensity_bckgrd = []

# for i in np.arange(0, len(Q), 20):
#     Q_bckgrd.append(Q[i])
#     intensity_bckgrd.append(intensity[i])
#
# Q = np.array(Q_bckgrd)
# intensity = np.array(intensity_bckgrd)

x0 = [639.05436108,  238.29655869,  173.94522173, -111.77924248,  13.81729277,  0, 0]


result = minimize(object_func, x0)

bckgrd = func(Q, result.x)

plt.plot(Q, bckgrd, 'o')
plt.plot(Q, intensity)
plt.figure(4)
plt.plot(Q, intensity - bckgrd)