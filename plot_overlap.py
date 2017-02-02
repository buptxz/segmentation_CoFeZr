# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 17:27:27 2016

@author: fangren
"""


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec



path = 'C:\\Research_FangRen\Data\\July2016\\CoVZr_ternary\\1Dfiles\\\
Annealing_pair_14_7_14\\scan77\\'

filename1 = 'Sample14_7thin_24x24_t30_0077_bckgrd_subtracted.csv'
filename2 = 'Sample15_7thick_24x24_t30_0077_bckgrd_subtracted.csv' 
filename3 = 'Sample7_annealed_24x24_t30_0077_bckgrd_subtracted.csv'
filename4 = 'Sample14_annealed_24x24_t30_0077_bckgrd_subtracted.csv'
filename5 = 'Sample15_annealed_24x24_t30_0077_bckgrd_subtracted.csv'

#f, (ax, ax2) = plt.subplots(2, 1, sharex=True)


fullname = path + filename1
spectrum = np.genfromtxt(fullname, delimiter=',', skip_header = 0)
IntAve = spectrum[:,1]
Qlist = spectrum[:,0]
plt.plot(Qlist, IntAve, label = '100 nm')

fullname = path + filename2
spectrum = np.genfromtxt(fullname, delimiter=',', skip_header = 0)
IntAve = spectrum[:,1]/5
Qlist = spectrum[:,0]
plt.plot(Qlist, IntAve, label = '500 nm')

fullname = path + filename3
spectrum = np.genfromtxt(fullname, delimiter=',', skip_header = 0)
IntAve = spectrum[:,1]
Qlist = spectrum[:,0]
plt.plot(Qlist, IntAve, label = '100 nm, 600 C')

fullname = path + filename4
spectrum = np.genfromtxt(fullname, delimiter=',', skip_header = 0)
IntAve = spectrum[:,1]
Qlist = spectrum[:,0]
plt.plot(Qlist, IntAve, label = '100 nm, 750 C')

fullname = path + filename5
spectrum = np.genfromtxt(fullname, delimiter=',', skip_header = 0)
IntAve = spectrum[:,1]/5
Qlist = spectrum[:,0]
plt.plot(Qlist, IntAve, label = '500 nm, 750 C')

plt.xlim((1.5, 4.5))
plt.ylim((-50, 800))
plt.ylabel('Intensity')
plt.xlabel('Q')
plt.legend()
plt.grid()


#
#
#ax2.set_ylim((-50, 1550))
#ax2.set_xlim((0.64, 5.8))
#
#ax.plot(Qlist, IntAve, 'm', label = '500 nm, 750 C', )
#
#ax.set_ylim((3400, 3700))
#ax.set_xlim((0.64, 5.8))
#
## hide the spines between ax and ax2
#ax.spines['bottom'].set_visible(False)
#ax2.spines['top'].set_visible(False)
#ax.xaxis.tick_top()
#ax.tick_params(labeltop='off')  # don't put tick labels at the top
#ax2.xaxis.tick_bottom()
#
#d = .015  # how big to make the diagonal lines in axes coordinates
## arguments to pass plot, just so we don't keep repeating them
#kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
#ax.plot((-d, +d), (-d, +d), **kwargs)        # top-left diagonal
#ax.plot((1 - d, 1 + d), (-d, +d), **kwargs)  # top-right diagonal
#
#kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
#ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left diagonal
#ax2.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)  # bottom-right diagonal
#
## What's cool about this is that now if we vary the distance between
## ax and ax2 via f.subplots_adjust(hspace=...) or plt.subplot_tool(),
## the diagonal lines will move accordingly, and stay right at the tips
## of the spines they are 'breaking'
#
#plt.show()