# -*- coding: utf-8 -*-
"""
Created on Wed Aug 03 14:03:38 2016

@author: Tri Duong
"""

import os
import math
import glob
import pandas as pd
import numpy as np
from scipy.spatial import distance

path = 'C:\\Research_FangRen\\Data\\July2016\\CoZrFe_ternary\\1D\\Sample3\\'
base_filename = 'Sample3_24x24_t30_'

def concatenate(path):
    """
    concatenate all the csv files in a folder, return a 2D dataframe
    """
    os.chdir(path)
    fileList=glob.glob("*.csv")
    dfList=[]
    for filename in fileList:
        if filename[-5] == 'a':
            meta_data = np.genfromtxt(filename, delimiter=',', skip_header = 0)
            scan_register = meta_data[:, 0]
        elif filename[-5] == 'D':
            df=pd.read_csv(filename,header=None,usecols=(1,),skiprows=4)
            dfList.append(df)
    return dfList, list(scan_register)
     
def find_neighbour(index, scan_register, length_of_row):
    """
    return the neighbour directly to right of the desired index and neighbour directly underneath the desired index
    """
    register = scan_register[index]
    register_neighbour1 = register + 1
    register_neighbour2 = register + length_of_row
    try:
        index_neighbour1 = scan_register.index(register_neighbour1) 
        index_neighbour2 = scan_register.index(register_neighbour2) 
    except ValueError:
        index_neighbour1 = index
        index_neighbour2 = index
    return index,index_neighbour1, index_neighbour2

    
def add_feature_to_master(feature, base_filename, folder_path, save_path):
    """
    add a feature 'feature' to master meta data, feature is in the form of a ziped row
    """
    feature = np.array([feature]) 
    os.chdir(path)
    fileList=glob.glob("*.csv")
    for filename in fileList:
        if filename[-5] == 'a':
                master_data = np.genfromtxt(filename, delimiter=',', skip_header = 1)
    master_data = np.nan_to_num(master_data)
    print master_data.shape, feature.T.shape
    #print dimension, master_data[:dimension:].shape, feature[:dimension:].shape
    master_data = np.concatenate((master_data, feature.T), axis = 1)
    print master_data.shape
    np.savetxt(save_path + base_filename + 'near_neighbor_distances.csv', master_data, \
    delimiter=",", header="register#,plate_x,plate_y,Seconds,i0,i1,mon,bstop,Omron,CH6,\
    CH7,TEMP,marccd,ICRxT,OCRxT,ROI1,ROI2,ROI3,ROI4,ROI5,ROI6,ROI7,ROI8,ROI9,\
    ROI10,RIO11,ROI12,ROI13,SWX,CCD1,CTEMP,Timer,pd1,pd2,pd3,pd4,pd5,pd6,pd7,\
    pd8,pd9,pd10,pd11,pd12,pd13,pd14,pd15,pd16,scan#,Imax,Iave,ratio,scan#,texture, \
    Co, Fe, Zr, peak_position, peak_width, peak_intensity, distances")


dfList, scan_register = concatenate(path)
"""
    Implement the find_neighbour function to call the file sample and perform any desire distance metric comparision 
    Remember to change the index range (line 96) and length of rows (line 97) base on the type of wafer sample
"""
emDist=[]
output=[]
for index in range(441): 
    x=find_neighbour(index, scan_register, 31) 
    emDist.append(x)
    data1=dfList[x[0]]
    data2=dfList[x[1]]
    data3=dfList[x[2]] 
    x=distance.cosine(data1,data2)
    y=distance.cosine(data1,data3)
    w=math.sqrt((x**2)+(y**2))
    output.append(w)
    index=index+1

add_feature_to_master(output, base_filename, path, path)

"""
Plot distance heat map according to the masterdata file
"""
