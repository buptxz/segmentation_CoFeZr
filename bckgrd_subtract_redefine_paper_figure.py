"""
Created on Feb 8, 2017

@author: fangren
"""

import os.path
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import basinhopping
from scipy.interpolate import interp1d
from numpy.polynomial.chebyshev import chebval


def set_window(windows_size, Q_original, intensity_original):
    Q = []
    intensity = []
    for i in np.arange(0, len(Q_original), windows_size):
        Q.append(Q_original[i])
        intensity.append(intensity_original[i])
    Q = np.array(Q)
    intensity = np.array(intensity)
    return Q, intensity

def file_index(index):
    if len(str(index)) == 1:
        return '000' + str(index)
    elif len(str(index)) == 2:
        return '00' + str(index)
    elif len(str(index)) == 3:
        return '0' + str(index)
    elif len(str(index)) == 4:
        return str(index)

def func(x, *params):
    params = params[0]
    y = chebval(x, params[:4])
    E = params[4]
    y = y + E /x
    return y

def object_func(*params):
    params = params[0]
    J = 0
    fit = chebval(Q, params[:4])
    E = params[4]
    fit = fit + E/Q
    for i in range(len(intensity)):
        if Q[i] < 1:
            if intensity[i] < fit[i]:
                J = J + (intensity[i]-fit[i])**4
            elif intensity[i] >= fit[i]:
                J = J + (intensity[i]-fit[i])**4
        else:
            if intensity[i] < fit[i]:
                J = J + (intensity[i] - fit[i]) ** 4
            elif intensity[i] >= fit[i]:
                J = J + (intensity[i] - fit[i]) ** 2
    return J


# set folder and save path
path = 'C:\\Research_FangRen\\Data\\Metallic_glasses_data\\CoZrFe_ternary\\1D\\raw_1D'
save_path = 'C:\\Research_FangRen\\Data\\Metallic_glasses_data\\CoZrFe_ternary\\Masterfiles\\high\\plots\\'
basename = 'Sample3_24x24_t30_'

# 1
file_name = os.path.join(path, basename + file_index(1) + '_1D.csv')
spectrum = np.genfromtxt(file_name, delimiter= ',')
intensity_original = spectrum[:, 1][30:-70]
Q_original =  spectrum[:, 0][30:-70]

# create a sparse set of data for fitting, window size: 20
Q, intensity = set_window(20, Q_original, intensity_original)

# fit  the result according the the defined object_func with the initialized parameters and bounds
x0 = [1, 1, 1, 1, 1]
result = basinhopping(object_func, x0)
bckgrd_sparse = func(Q, result.x)
f = interp1d(Q, bckgrd_sparse, kind='cubic', bounds_error=False)
bckgrd = f(Q_original)

# save the plot
plt.figure(1, figsize = (5, 6))
plt.subplot(421)
plt.plot(Q_original, intensity_original, 'b')
plt.plot(Q, intensity, 'o',  c = 'g', markersize = 2)
plt.plot(Q, bckgrd_sparse, 'o', c = 'r', markersize = 2)
plt.xlim(0.8, 5.8)
plt.subplot(423)
plt.plot(Q_original, intensity_original-bckgrd, 'm')
plt.plot(Q, [0] * len(Q), 'r--')
plt.xlim(0.8, 5.8)


# 2
file_name = os.path.join(path, basename + file_index(2) + '_1D.csv')
spectrum = np.genfromtxt(file_name, delimiter= ',')
intensity_original = spectrum[:, 1][30:-70]
Q_original =  spectrum[:, 0][30:-70]

# create a sparse set of data for fitting, window size: 20
Q, intensity = set_window(20, Q_original, intensity_original)

# fit  the result according the the defined object_func with the initialized parameters and bounds
x0 = [1, 1, 1, 1, 1]
result = basinhopping(object_func, x0)
bckgrd_sparse = func(Q, result.x)
f = interp1d(Q, bckgrd_sparse, kind='cubic', bounds_error=False)
bckgrd = f(Q_original)

# save the plot
plt.subplot(422)
plt.plot(Q_original, intensity_original, 'b')
plt.plot(Q, intensity, 'o', c = 'g', markersize = 2)
plt.plot(Q, bckgrd_sparse, 'o', c = 'r', markersize = 2)
plt.xlim(0.8, 5.8)
plt.subplot(424)
plt.plot(Q_original, intensity_original-bckgrd, 'm')
plt.plot(Q, [0] * len(Q), 'r--')
plt.xlim(0.8, 5.8)

# 3
file_name = os.path.join(path, basename + file_index(256) + '_1D.csv')
spectrum = np.genfromtxt(file_name, delimiter= ',')
intensity_original = spectrum[:, 1][30:-70]
Q_original =  spectrum[:, 0][30:-70]

# create a sparse set of data for fitting, window size: 20
Q, intensity = set_window(20, Q_original, intensity_original)

# fit  the result according the the defined object_func with the initialized parameters and bounds
x0 = [1, 1, 1, 1, 1]
result = basinhopping(object_func, x0)
bckgrd_sparse = func(Q, result.x)
f = interp1d(Q, bckgrd_sparse, kind='cubic', bounds_error=False)
bckgrd = f(Q_original)

# save the plot
plt.subplot(425)
plt.plot(Q_original, intensity_original, 'b')
plt.plot(Q, intensity, 'o', c='g', markersize = 2)
plt.plot(Q, bckgrd_sparse, 'o', c = 'r', markersize = 2)
plt.xlim(0.8, 5.8)
plt.subplot(427)
plt.plot(Q_original, intensity_original-bckgrd, 'm')
plt.plot(Q, [0] * len(Q), 'r--')
plt.xlim(0.8, 5.8)

# 4
file_name = os.path.join(path, basename + file_index(257) + '_1D.csv')
spectrum = np.genfromtxt(file_name, delimiter= ',')
intensity_original = spectrum[:, 1][30:-70]
Q_original =  spectrum[:, 0][30:-70]

# create a sparse set of data for fitting, window size: 20
Q, intensity = set_window(20, Q_original, intensity_original)

# fit  the result according the the defined object_func with the initialized parameters and bounds
x0 = [1, 1, 1, 1, 1]
result = basinhopping(object_func, x0)
bckgrd_sparse = func(Q, result.x)
f = interp1d(Q, bckgrd_sparse, kind='cubic', bounds_error=False)
bckgrd = f(Q_original)

# save the plot
plt.subplot(426)
plt.plot(Q_original, intensity_original, 'b')
plt.plot(Q, intensity, 'o', c='g', markersize = 2)
plt.plot(Q, bckgrd_sparse, 'o', c = 'r', markersize = 2)
plt.xlim(0.8, 5.8)
plt.subplot(428)
plt.plot(Q_original, intensity_original-bckgrd, 'm')
plt.plot(Q, [0] * len(Q), 'r--')
plt.xlim(0.8, 5.8)



plt.savefig(os.path.join(save_path, basename + 'figure.png'), dpi = 600)
plt.close('all')
#
