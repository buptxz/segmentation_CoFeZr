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
import os.path


def func(x, *params):
    """
    create a Lorentzian fitted curve according to params
    """
    y = np.zeros_like(x)
    for i in range(0, len(params), 4):
        ctr = params[i]
        amp = params[i+1]
        wid = params[i+2]
        n = params[i+3]
        y = y + n * amp * np.exp(-4 * np.log(2) * ((x - ctr) / wid) ** 2) + (1 - n) * amp * wid ** 2 / 4 / (
        (x - ctr) ** 2 + wid ** 2 / 4)
    return y


path = 'C:\\Research_FangRen\Data\\Metallic_glasses_data\\CoZrFe_ternary\\1D\\bckgrd_subtracted_1D\\'
save_path = 'C:\\Research_FangRen\\Data\\Metallic_glasses_data\\CoZrFe_ternary\\1D\\peak_fitting_voigt\\'

guess = [ 3.1, 5000, 0.33, 0.5]
high = [3.4, 10000, 0.8, 1]
low = [2.1, 0, 0, 0]


for filename in glob.glob(os.path.join(path, '*.csv')):     
    if basename(filename)[-5] == 'd':
        print 'processing', filename
        try:
            data = np.genfromtxt(filename, delimiter = ',' )
            Qlist = data[:,0][:-19]
            IntAve = data[:,1][:-19]
            
            popt, pcov = curve_fit(func, Qlist, IntAve, p0=guess, bounds = (low, high))
            fit = func(Qlist, *popt)
            plt.figure(1)            
            plt.plot(Qlist, IntAve)
            plt.plot( Qlist, fit)
            ctr1 = popt[0]
            amp1 = popt[1]
            wid1 = popt[2]
            n1 = popt[3]
            curve1 = n1 * amp1 * np.exp( -4 * np.log(2) * ((Qlist - ctr1)/wid1)**2) + (1-n1) * amp1 * wid1**2 / 4 / ((Qlist-ctr1)**2 + wid1**2 / 4)
            plt.plot(Qlist, curve1)
            plt.show()
            plt.savefig(save_path + basename(filename)[:-4] + '_peak_fitting_Voigt.png')
            plt.close()
            
            popt = np.reshape(popt, (popt.size/4, 4))
            np.savetxt(save_path + basename(filename)[:-4] + '_peak_fitting_Voigt.csv', popt, delimiter=",")
            
        except RuntimeError:
            print "Failed to fit", filename
            print "used the previous peak information"
            np.savetxt(save_path + basename(filename)[:-4] + '_peak_fitting_Voigt.csv', popt, delimiter=",")
            
