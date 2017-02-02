# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 13:57:10 2016

@author: fangren
"""

import matplotlib.pyplot as plt
import numpy as np
import glob
import os
from os.path import basename

path = 'C:\\Research_FangRen\\Data\\July2016\\CoZrFe_ternary\\1D\\Sample16\\background_subtracted\\peak_fit_threePeaks_Voigt\\'


def file_index(index):
    if len(str(index)) == 1:
        return '000' + str(index)
    elif len(str(index)) == 2:
        return '00' + str(index)
    elif len(str(index)) == 3:
        return '0' + str(index)
    elif len(str(index)) == 4:
        return str(index)


index = 1
for filename in glob.glob(os.path.join(path, '*.png')):    
#    print basename(filename)[-45:-41], file_index(index)
    while basename(filename)[-45:-41] != file_index(index):
        print index 
        index += 1
    index += 1