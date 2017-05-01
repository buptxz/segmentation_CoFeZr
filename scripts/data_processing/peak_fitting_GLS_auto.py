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
from extract_peak_number import extract_peak_num


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


path = 'C:\\Research_FangRen\\Data\\Metallic_glasses_data\\CoZrFe_ternary\\1D\\bckgrd_subtracted_1D\\'
save_path = 'C:\\Research_FangRen\\Data\\Metallic_glasses_data\\CoZrFe_ternary\\1D\\peak_fitting_test\\'

for filename in glob.glob(os.path.join(path, '*.csv')):
    if basename(filename)[-5] == 'd':
        print 'processing', filename
        data = np.genfromtxt(filename, delimiter=',')
        Qlist = data[:, 0][:647]
        IntAve = data[:, 1][:647]
        try:
            data = np.genfromtxt(filename, delimiter=',')
            Qlist = data[:, 0][:647]
            IntAve = data[:, 1][:647]
            newRow, peaks = extract_peak_num(Qlist, IntAve, 0, a1=15, a2=20)

            guess = []
            low = []
            high = []
            print peaks

            for peak in peaks:
                guess.append(Qlist[peak])
                guess.append(IntAve[peak])
                guess.append(0.2)
                guess.append(0.5)
            print guess
            print len(guess)
            popt, pcov = curve_fit(func, Qlist, IntAve, p0=guess)
            fit = func(Qlist, *popt)

            plt.figure(1)
            plt.plot(Qlist, IntAve, 'k')
            plt.plot(Qlist, fit, 'b')

            curve = np.zeros_like(Qlist)
            for i in range(0, len(popt), 4):
                ctr = popt[i]
                amp = popt[i + 1]
                wid = popt[i + 2]
                n = popt[i + 3]
                curve = curve + n * amp * np.exp(-4 * np.log(2) * ((Qlist - ctr) / wid) ** 2) + (1 - n) * amp * wid ** 2 / 4 / (
                    (Qlist - ctr) ** 2 + wid ** 2 / 4)
                plt.plot(Qlist, curve)
            plt.savefig(save_path + basename(filename)[:-4] + '_peak_analysis_GLS')
            plt.close()

            popt = np.reshape(popt, (popt.size / 4, 4))
            np.savetxt(save_path + basename(filename)[:-4] + '_peak_analysis_GLS.csv', popt, delimiter=",")
        except RuntimeError:
            print "Failed to fit", filename
            print "used the previous peak information"
            # np.savetxt(save_path + basename(filename)[:-4] + '_peak_analysis_GLS.csv', popt, delimiter=",")




