# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 18:34:53 2016

@author: fangren
"""

"""
find indices
"""

import numpy as np
import imp

plotTernary = imp.load_source("plt_ternary_save", "plotTernary.py")


path = 'C:\\Research_FangRen\\Data\\July2016\\CoVZr_ternary\\masterfiles\\Comparing_low_high\\'

filename_low = 'CLEANED_All_Sample9_10_18_master_metadata_low.csv'
filename_high = 'CLEANED_All_Sample8_14_17_master_metadata_high.csv'

data_low = np.genfromtxt(path+filename_low, delimiter=',', skip_header = 1)
data_high = np.genfromtxt(path+filename_high, delimiter=',', skip_header = 1)

Co_low = data_low[:,54]
V_low = data_low[:,55]
Zr_low = data_low[:,56]
width_low = data_low[:,58]

Co_high = data_high[:,54]
V_high = data_high[:,55]
Zr_high = data_high[:,56]
width_high = data_high[:,58]

Co = []
V = []
Zr = []
width_diff = []

for i in range(len(Co_high)):
    for j in range(len(Co_low)):
        if np.abs(Co_high[i] - Co_low[j]) < 1.5 and np.abs(V_high[i] - V_low[j]) < 1.5 and np.abs(Zr_high[i] - Zr_low[j]) < 1.5:
            Zr.append(Zr_high[i])
            V.append(V_high[i])
            Co.append(Co_high[i])
            width_diff.append(width_low[j] - width_high[i])

ternary_data = np.concatenate(([Co],[V],[Zr],[width_diff]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
                       sv=True, svpth=path, svflnm='wid_difference',
                       cbl='Scale', vmax = 0.12, vmin = -0.025, cmap='jet', cb=True, style='h')
