# -*- coding: utf-8 -*-
"""
Created on Tue Aug 02 13:19:54 2016

@author: fangren
"""

"""
need to run gap_statistics.py first
"""


import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import imp
import glob
import os
import csv
import numpy as np

plotTernary = imp.load_source("plt_ternary_save", "plotTernary.py")


def kmeans_clustering(data, cluster_num):
    kmeans = KMeans(n_clusters = cluster_num)
    kmeans.fit(data)
    labels = kmeans.labels_
    return labels


def addLabels(labels, folder_path, save_path):
    """
    add Imax, I column to an existing CSV spreadsheet
    create three lists for plotting: plate_x, plate_y, ratio of Imax and Iave
    ROI1, ROI2...
    """
    labels = np.concatenate((['labels',], labels))    
    for filename in glob.glob(os.path.join(folder_path, '*.csv')):
        if filename[-5] == 'h':
            print filename
            with open(filename, 'rb') as csvinput:
                with open(save_path+'k_clustering.csv', 'wb') as csvoutput:
                    reader = csv.reader(csvinput, delimiter = ',')
                    writer = csv.writer(csvoutput, delimiter = ',', lineterminator = '\n')
                    for row, label in zip(reader, labels):
                        row = row + list(str(label))
                        writer.writerow(row)


def twoD_visualize(folder_path):
    """
    create three lists for plotting: plate_x, plate_y, ROI1, ROI2, ROI3...
    """
    for filename in glob.glob(os.path.join(folder_path, '*.csv')):
        if filename[-5] == 'g':
            print filename
            data = np.genfromtxt(filename, delimiter=',', skip_header = 0)
            plate_x = data[:,1]
            plate_y = data[:,2]
            plate_x = np.nan_to_num(plate_x)
            plate_y = np.nan_to_num(plate_y)
            metal1 = data[:,54]
            metal2 = data[:,55]
            metal3 = data[:,56]
    return plate_x, plate_y, metal1, metal2, metal3
                 

cluster_num = input('cluster number =  ')
plt.close('all')


labels = kmeans_clustering(data, cluster_num)
addLabels(labels, folder_path, save_path)
plate_x, plate_y, metal1, metal2, metal3 = twoD_visualize(save_path)

#
#plt.figure(1, figsize = (9, 8.5))
#plt.scatter(plate_y, plate_x, c = labels, s = 400, marker = 's')
#plt.xlim((-36, 36))
#plt.ylim((-36, 36))
#plt.xlabel('plate_y')
#plt.ylabel('plate_x(flat)')


ternary_data = np.concatenate(([metal1],[metal2],[metal3],[labels]), axis = 0)
ternary_data = np.transpose(ternary_data)


plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','Fe','Zr'), scale=100,
                       sv=False, svpth=folder_path, svflnm='k_means',
                       cbl='Scale', cmap='jet', cb=True, style='h')