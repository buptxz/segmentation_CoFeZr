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

def file_index(index):
    if len(str(index)) == 1:
        return '000' + str(index)
    elif len(str(index)) == 2:
        return '00' + str(index)
    elif len(str(index)) == 3:
        return '0' + str(index)
    elif len(str(index)) == 4:
        return str(index)

# initialize parameters and high/low bounds
x0 = np.ones(45)
x0 = np.concatenate((x0, [300]))

low = np.ones(45)-0.05
low = np.concatenate((low, [0]))

high = np.ones(45)+0.05
high = np.concatenate((high, [2000]))

limit = []
for i in range(len(low)):
    limit.append((low[i], high[i]))


# set folder and save path
path = 'C:\\Research_FangRen\\Data\\Metallic_glasses_data\\CoZrFe_ternary\\1D\\raw_1D'
save_path = 'C:\\Research_FangRen\Data\\Metallic_glasses_data\\CoZrFe_ternary\\1D\\bckgrd_subtracted_1D'
basename = 'Sample16_2thin_24x24_t30_'
silicon_file = os.path.join(path, basename + '0233_1D.csv')
silicon_spectrum = np.genfromtxt(silicon_file, delimiter= ',')
Q = silicon_spectrum[:, 0][30:-70]
silicon = silicon_spectrum[:, 1][30:-70]



index = 1
total_num_scan = 441
while (index <= total_num_scan):
    file_name = os.path.join(path, basename + file_index(index) + '_1D.csv')
    print 'processing', file_name
    if os.path.exists(file_name):
        spectrum = np.genfromtxt(file_name, delimiter= ',')
        intensity = spectrum[:, 1][30:-70]

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


        # fit  the result according the the defined object_func with the initialized parameters and bounds
        result = minimize(object_func, x0, bounds=limit)
        bckgrd_sparse = silicon_bckgrd(result.x)
        f = interp1d(Q_sparse, bckgrd_sparse, kind = 'cubic', bounds_error = False)
        bckgrd = f(Q)

        # save the plot
        plt.subplot(211)
        plt.plot(Q, intensity)
        plt.plot(Q, bckgrd)
        plt.xlim(0.8, 5.8)
        plt.subplot(212)
        plt.plot(Q, intensity-bckgrd)
        plt.plot(Q, [0] * len(Q), 'r--')
        plt.xlim(0.8, 5.8)
        plt.savefig(os.path.join(save_path, basename + file_index(index) + '_bckgrd_subtracted.png'))
        plt.close('all')
        np.savetxt(os.path.join(save_path, basename + file_index(index) + '_bckgrd_subtracted.csv'), np.concatenate(([Q], [intensity - bckgrd])).T, delimiter= ',')
        index += 1
