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
path = '..\\..\\data\\raw_1D\\'
save_path = '..\\..\\figures\\'
basename = 'Sample3_24x24_t30_'


plt.figure(1, figsize = (10, 8))

# # 1
# file_name = os.path.join(path, basename + file_index(1) + '_1D.csv')
# spectrum = np.genfromtxt(file_name, delimiter= ',')
# intensity_original = spectrum[:, 1][30:-70]
# Q_original =  spectrum[:, 0][30:-70]
#
# # create a sparse set of data for fitting, window size: 20
# Q, intensity = set_window(20, Q_original, intensity_original)
#
# # fit  the result according the the defined object_func with the initialized parameters and bounds
# x0 = [1, 1, 1, 1, 1]
# result = basinhopping(object_func, x0)
# bckgrd_sparse = func(Q, result.x)
# f = interp1d(Q, bckgrd_sparse, kind='cubic', bounds_error=False)
# bckgrd = f(Q_original)
#
# # save the plot
#
# plt.subplot(421)
# plt.plot(Q_original, intensity_original, 'b', label = 'spectrum')
# plt.plot(Q, intensity, 'o',  c = 'r', markersize = 4, label = 'selected points')
# plt.plot(Q, bckgrd_sparse, 'o', c = 'g', markersize = 4, label = 'background')
# plt.legend()
# plt.xlim(0.8, 5.8)
# plt.subplot(422)
# plt.plot(Q_original, intensity_original-bckgrd, 'm', label = 'background subtracted')
# plt.plot(Q, [0] * len(Q), 'g--')
# plt.legend(loc = 1)
# plt.xlim(0.8, 5.8)
# plt.ylim(-10, 200)


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
plt.subplot(323)
plt.plot(Q_original, intensity_original, 'b', label = 'spectrum')
plt.plot(Q, intensity, 'o',  c = 'r', markersize = 4, label = 'selected points')
plt.plot(Q, bckgrd_sparse, 'o', c = 'g', markersize = 4, label = 'background')
plt.legend()
plt.xlim(0.8, 5.8)
plt.subplot(324)
plt.plot(Q_original, intensity_original-bckgrd, 'm', label = 'background subtracted')
plt.plot(Q, [0] * len(Q), 'g--')
plt.legend(loc = 1)
plt.xlim(0.8, 5.8)
plt.ylim(-10, 300)

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
plt.subplot(325)
plt.plot(Q_original, intensity_original, 'b', label = 'spectrum')
plt.plot(Q, intensity, 'o',  c = 'r', markersize = 4, label = 'selected points')
plt.plot(Q, bckgrd_sparse, 'o', c = 'g', markersize = 4, label = 'background')
plt.legend()
plt.xlim(0.8, 5.8)
plt.subplot(326)
plt.plot(Q_original, intensity_original-bckgrd, 'm', label = 'background subtracted')
plt.plot(Q, [0] * len(Q), 'g--')
plt.legend(loc = 1)
plt.xlim(0.8, 5.8)
plt.ylim(-5, 75)

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
plt.subplot(321)
plt.plot(Q_original, intensity_original, 'b', label = 'spectrum')
plt.plot(Q, intensity, 'o',  c = 'r', markersize = 4, label = 'selected points')
plt.plot(Q, bckgrd_sparse, 'o', c = 'g', markersize = 4, label = 'background')
plt.legend()
plt.xlim(0.8, 5.8)
plt.subplot(322)
plt.plot(Q_original, intensity_original-bckgrd, 'm', label = 'background subtracted')
plt.plot(Q, [0] * len(Q), 'g--')
plt.legend(loc = 1)
plt.xlim(0.8, 5.8)
plt.ylim(-100, 2000)


plt.savefig(os.path.join(save_path, 'Figure1_background_subtraction.png'), dpi = 300)
# plt.close('all')
#
