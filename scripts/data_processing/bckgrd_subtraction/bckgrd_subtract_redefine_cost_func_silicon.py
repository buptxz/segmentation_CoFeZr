"""
Created on Feb 8, 2017

@author: fangren
"""

import os.path
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize
from scipy.interpolate import interp1d

def silicon_bckgrd(*params):
    params = params[0]
    fit = []
    for i in range(len(params)-1):
        fit.append(params[i]*silicon_sparse[i])
    fit = fit + params[-1]
    return fit

def object_func(*params):
    params = params[0]
    J = 0
    fit = silicon_bckgrd(params)
    for i in range(len(intensity_sparse)):
        if intensity_sparse[i] < fit[i]:
            J = J + (intensity_sparse[i] - fit[i]) ** 4
        elif intensity_sparse[i] >= fit[i]:
            J = J + (intensity_sparse[i] - fit[i]) ** 2
    return J

# import data
path = 'C:\\Research_FangRen\\Data\\Metallic_glasses_data\\CoZrFe_ternary\\1D\\raw_1D'
spectrum_file = os.path.join(path, 'Sample3_24x24_t30_0400_1D.csv')
silicon_file = os.path.join(path, 'Sample3_24x24_t30_0256_1D.csv')

spectrum = np.genfromtxt(spectrum_file, delimiter= ',')
silicon_spectrum = np.genfromtxt(silicon_file, delimiter= ',')

Q = spectrum[:, 0][30:-70]
intensity = spectrum[:, 1][30:-70]
silicon = silicon_spectrum[:, 1][30:-70]


# create a sparse set of data for fitting, stepsize: 20
Q_sparse = []
intensity_sparse = []
silicon_sparse = []

for i in np.arange(0, len(Q), 20):
    Q_sparse.append(Q[i])
    silicon_sparse.append(silicon[i])
    intensity_sparse.append(intensity[i])

Q_sparse = np.array(Q_sparse)
silicon_sparse = np.array(silicon_sparse)
intensity_sparse = np.array(intensity_sparse)


# initialize parameters and high/low bounds
x0 = np.ones(len(silicon_sparse))
x0 = np.concatenate((x0, [300]))

low = np.ones(len(silicon_sparse))-0.05
low = np.concatenate((low, [0]))

high = np.ones(len(silicon_sparse))+0.05
high = np.concatenate((high, [2000]))

limit = []
for i in range(len(low)):
    limit.append((low[i], high[i]))

# fit  the result according the the defined object_func with the initialized parameters and bounds
result = minimize(object_func, x0, bounds=limit)
bckgrd_sparse = silicon_bckgrd(result.x)

f = interp1d(Q_sparse, bckgrd_sparse, kind = 'cubic', bounds_error = False)
bckgrd = f(Q)


plt.figure(1)
plt.plot(Q, bckgrd, 'o')
plt.plot(Q, intensity)

plt.figure(2)
plt.plot(Q, intensity - bckgrd)
plt.plot(Q, [0]*len(Q), 'r--')