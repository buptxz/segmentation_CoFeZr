"""
Created on Feb 8, 2017

@author: fangren
"""

import os.path
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize, basinhopping

path = 'C:\\Research_FangRen\\Data\\Metallic_glasses_data\\CoZrFe_ternary\\1D\\raw_1D'

# spectrum
spectrum_file = os.path.join(path, 'Sample3_24x24_t30_0257_1D.csv')
spectrum = np.genfromtxt(spectrum_file, delimiter= ',')

# import data from the spectrum
Q_original = spectrum[:, 0][30:-70]
intensity_original = spectrum[:, 1][30:-70]

Q = []
intensity = []
for i in np.arange(0, len(Q_original), 20):
    Q.append(Q_original[i])
    intensity.append(intensity_original[i])
Q = np.array(Q)
intensity = np.array(intensity)


def func(x, *params):
    params = params[0]
    A = params[0]
    B = params[1]
    C = params[2]
    D = params[3]
    E = params[4]
    y = A + B*x + C * (x**2) + D * (x**3) + E /x
    return y

def object_func(*params):
    params = params[0]
    J = 0
    A = params[0]
    B = params[1]
    C = params[2]
    D = params[3]
    E = params[4]
    fit = A + B*Q + C * (Q**2) + D * (Q**3) + E/Q
    for i in range(len(intensity)):
        if Q[i] < 1:
            if intensity[i] < fit[i]:
                J = J + (intensity[i]-fit[i])**4
            elif intensity[i] >= fit[i]:
                J = J + (intensity[i]-fit[i])**4
        elif Q[i] >= 1 and Q[i] < 5.5:
            if intensity[i] < fit[i]:
                J = J + (intensity[i] - fit[i]) ** 4
            elif intensity[i] >= fit[i]:
                J = J + (intensity[i] - fit[i]) ** 2
        else:
            if intensity[i] < fit[i]:
                J = J + (intensity[i] - fit[i]) ** 4
            elif intensity[i] >= fit[i]:
                J = J + (intensity[i] - fit[i]) ** 4
    return J


# x0 = [639.05436108,  238.29655869,  173.94522173, -111.77924248, 0]
x0 = [1,1,1,1, 1]

result = basinhopping(object_func, x0)
bckgrd = func(Q, result.x)

plt.plot(Q_original, intensity_original)
plt.plot(Q, intensity, 'o')
plt.plot(Q, bckgrd, 'o', c = 'r')


# plt.figure(4)
# plt.plot(Q, intensity - bckgrd)