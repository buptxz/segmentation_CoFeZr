# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 18:34:53 2016

@author: fangren
"""

"""
find indices
"""

import numpy as np

path = 'C:\\Research_FangRen\\Data\\July2016\\CoZrFe_ternary\\Masterfiles\\high\\ploting\\'

filename = 'CLEANED_Sample3_24x24_t30_36410038master_metadata.csv'
#filename = 'CLEANED_Sample1_24x24_t30_14715979master_metadata.csv'

data = np.genfromtxt(path+filename, delimiter=',', skip_header = 1)

Co = data[:,54]
Fe = data[:,55]
Zr = data[:,56]
scan_num = data[:,52]

scan_chosen = []
indices = []
for i in range(len(scan_num)):
    if Co[i]/Fe[i] < 1.957 and Co[i]/Fe[i] > 1.757:
        scan_chosen.append(scan_num[i])
        indices.append(i)

scan_chosen = map(int, scan_chosen)

scan_chosen = sorted(scan_chosen)
print scan_chosen


print Zr[indices]

