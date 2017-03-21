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
    create a Lorentzian fitted curve according to params
    """
    y = np.zeros_like(x)
    ctr1 = params[0]
    amp1 = params[1]
    wid1 = params[2]
    ctr2 = params[3]
    amp2 = params[1] / 2
    wid2 = params[4]
    ctr3 = params[5]
    amp3 = params[6]
    wid3 = params[7]
    ctr4 = params[8]
    amp4 = params[9]
    wid4 = params[10]
    amp5 = params[9]/2
    ctr5 = params[11]
    wid5 = params[12]
    ctr6 = params[13]
    amp6 = params[14]
    wid6 = params[15]
    y = y + \
        amp1 * np.exp( -((x - ctr1)/wid1)**2) + \
        amp2 * np.exp( -((x - ctr2)/wid2)**2) + \
        amp3 * np.exp( -((x - ctr3)/wid3)**2) + \
        amp4 * np.exp( -((x - ctr4)/wid4)**2) + \
        amp5 * np.exp( -((x - ctr5)/wid5)**2) + \
        amp6 * np.exp( -((x - ctr6)/wid6)**2)
    return y


guess = [640.2, 1000, 10,
         638.9, 10,
         705.4, 0, 10,
         692.7, 1000, 10,
         691.2, 10,
         772.4, 0, 10]
high = [642.2, 50000, 30,
        640.9, 30,
        707.4, 50000, 30,
        694.7, 50000, 30,
        693.18, 30,
        774.35, 50000, 50]
low = [638.2, 0, 10,
       636.9, 10,
       703.4, 0, 10,
       690.7, 0, 10,
       689.18, 10,
       764.35, 0, 10]


path = 'C:\\Research_FangRen\\XRF_Co_Fe_Zr\\mca_files\\'
base_filename = 'Sample16_2thin_24x24_t30_scan1_mca.dat'

filename = path + base_filename

save_path = path + 'Sample16_peak_fit\\'
if not os.path.exists(save_path):
    os.makedirs(save_path)

data = np.genfromtxt(filename, delimiter=' ')
x = np.array(range(data.shape[1]))

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
        amp2 = popt[1]/2
        wid2 = popt[4]
        ctr3 = popt[5]
        amp3 = popt[6]
        wid3 = popt[7]
        ctr4 = popt[8]
        amp4 = popt[9]
        wid4 = popt[10]
        ctr5 = popt[11]
        amp5 = popt[9] / 2
        wid5 = popt[12]
        ctr6 = popt[13]
        amp6 = popt[14]
        wid6 = popt[15]
        curve1 = amp1 * np.exp( -((x - ctr1)/wid1)**2)
        curve2 = amp2 * np.exp( -((x - ctr2)/wid2)**2)
        curve3 = amp3 * np.exp( -((x - ctr3)/wid3)**2)
        curve4 = amp4 * np.exp( -((x - ctr4)/wid4)**2)
        curve5 = amp5 * np.exp( -((x - ctr5)/wid5)**2)
        curve6 = amp6 * np.exp( -((x - ctr6)/wid6)**2)
        plt.plot(x, curve1)
        plt.plot(x, curve2)
        plt.plot(x, curve4)
        plt.plot(x, curve3)
        plt.plot(x, curve5)
        plt.plot(x, curve6)
        plt.xlim(500, 1000)
        print 'saving', save_path + base_filename[:-13] + str(i) + '_peak_analysis'
        plt.savefig(save_path + base_filename[:-13] + str(i) + '_peak_analysis')
        plt.close()
        result = [[amp1, amp2, amp3+amp4+amp5, amp6], [ctr1, ctr2, (ctr4+ctr5+ctr3)/3, ctr6], [wid1, wid2, (wid4+wid5+wid3)/2, wid6]]
        np.savetxt(save_path + base_filename[:-13] + str(i) + '_peak_analysis.csv', result, delimiter=",")
    except RuntimeError:
        print "Failed to fit", i+1
        print "used the previous peak information"
        np.savetxt(save_path + base_filename[:-13] + str(i) + '_peak_analysis.csv', result, delimiter=",")

