# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 15:37:51 2016

@author: fangren
"""

import matplotlib.pyplot as plt
import numpy as np
import glob
import os
from os.path import basename
from scipy.optimize import curve_fit
import imp


def func(x, *params):
    """
    create a Gaussian fitted curve according to params
    """
    y = np.zeros_like(x)
    # Fe alpha
    ctr1 = params[0]
    amp1 = params[1]
    wid1 = params[2]
    # Fe beta, refer to the paper (Smith_et_al-1974-X-Ray_Spectrometry) for the value of beta/alpha ratio
    ctr2 = params[3]
    amp2 = params[1]*0.136
    wid2 = params[4]
    # Co alpha
    ctr3 = params[5]
    amp3 = params[6]
    wid3 = params[7]
    # Co beta, refer to the paper (Smith_et_al-1974-X-Ray_Spectrometry) for the value of beta/alpha ratio
    ctr4 = params[8]
    amp4 = params[6]* 0.137
    wid4 = params[9]

    y = y + \
        amp1 * np.exp( -((x - ctr1)/wid1)**2) + \
        amp2 * np.exp( -((x - ctr2)/wid2)**2) + \
        amp3 * np.exp( -((x - ctr3)/wid3)**2) + \
        amp4 * np.exp( -((x - ctr4)/wid4)**2)
    return y



# path
path = 'C:\\Research_FangRen\\Data\\Metallic_glasses_data\\CoZrFe_ternary\\XRF\\mca_files\\'
base_filename = 'Sample6_24x24_t30_scan1_mca.dat'

filename = path + base_filename
save_path = path + 'XRF_channels_fit_Sample6\\'
if not os.path.exists(save_path):
    os.makedirs(save_path)

data = np.genfromtxt(filename, delimiter=' ')
x = np.array(range(data.shape[1]))


# # visualize a few XRF spectra for defining peak positions.
# y1 = data[1, :]
# y2 = data[100, :]
# y3 = data[300, :]
# y4 = data[440, :]
# plt.plot(x, y1)
# plt.plot(x, y2)
# plt.plot(x, y3)
# plt.plot(x, y4)


# initialize guesses and high and low bounds for fitting, refer to the excel file for peak calibration
guess = [640, 1000, 10,
         705, 10,
         692, 1000, 10,
         764, 10]
high = [660, 50000, 30,
         725, 30,
         712, 50000, 30,
         784, 30]
low = [620, 0, 0,
         685, 0,
         672, 0, 0,
         744, 0]

# fitting starts from here
for i in range(1, data.shape[0]):
    print i
    intensity = data[i]
    try:
        popt, pcov = curve_fit(func, x, intensity, p0=guess, bounds = (low, high))
        fit = func(x, *popt)
        plt.figure(1)
        plt.plot(x, intensity)
        plt.plot(x, fit)
        ctr1 = popt[0]
        amp1 = popt[1]
        wid1 = popt[2]

        ctr2 = popt[3]
        amp2 = popt[1] * 0.136
        wid2 = popt[4]

        ctr3 = popt[5]
        amp3 = popt[6]
        wid3 = popt[7]

        ctr4 = popt[8]
        amp4 = popt[6] * 0.137
        wid4 = popt[9]

        curve1 = amp1 * np.exp( -((x - ctr1)/wid1)**2)
        curve2 = amp2 * np.exp( -((x - ctr2)/wid2)**2)
        curve3 = amp3 * np.exp( -((x - ctr3)/wid3)**2)
        curve4 = amp4 * np.exp( -((x - ctr4)/wid4)**2)

        plt.plot(x, curve1)
        plt.plot(x, curve2)
        plt.plot(x, curve4)
        plt.plot(x, curve3)

        plt.xlim(380, 1000)
        print 'saving', save_path + base_filename[:-13] + str(i) + '_XRF_fit'
        plt.savefig(save_path + base_filename[:-13] + str(i) + '_XRF_fit')
        plt.close()
        result = [[amp1, amp2, amp3, amp4], [ctr1, ctr2, ctr3, ctr4], [wid1, wid2, wid3, wid4]]
        np.savetxt(save_path + base_filename[:-13] + str(i) + '_XRF_fit.csv', result, delimiter=",")
    except RuntimeError:
        print "Failed to fit", i+1
        print "used the previous peak information"
        np.savetxt(save_path + base_filename[:-13] + str(i) + '_XRF_fit.csv', result, delimiter=",")

