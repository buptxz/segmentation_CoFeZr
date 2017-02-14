"""
Created on Feb 8, 2017

@author: fangren
"""

import os.path
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


path = 'C:\\Research_FangRen\\Data\\Metallic_glasses_data\\CoZrFe_ternary\\1D\\raw_1D'
spectrum_file = os.path.join(path, 'Sample3_24x24_t30_0001_1D.csv')

spectrum = np.genfromtxt(spectrum_file, delimiter= ',')
Q = spectrum[:, 0][30:-70]
intensity = spectrum[:, 1][30:-70]



def func(x, *params):
    A = params[0]
    B = params[1]
    C = params[2]
    D = params[3]
    E = params[4]
    y = A + B/x + C*x + D * (x**2) + E * (x**3)
    return y


Q_bckgrd = []
intensity_bckgrd = []

for i in np.arange(0, len(Q), 80):
    Q_bckgrd.append(Q[i])
    intensity_bckgrd.append(intensity[i])


guess = (0,0,0,0,0)
popt, pcov = curve_fit(func, Q_bckgrd, intensity_bckgrd, p0=guess)

bckgrd = popt[0] + popt[1]/Q + popt[2]*Q + popt[3] * (Q**2) + popt[4] * (Q**3)

plt.plot(Q, bckgrd, 'o')
plt.plot(Q, intensity)
# plt.figure(4)
# plt.plot(Q, intensity - bckgrd)