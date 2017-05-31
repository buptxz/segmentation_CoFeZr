__author__ = "Travis Williams"
# University of South Carolina
# Jason Hattrick-Simpers group
# Starting Date: June, 2016

import matplotlib.pyplot as plt
import numpy as np

from scripts import ternary


def plt_ternary_save(data, tertitle='',  labelNames=('Species A','Species B','Species C'), scale=100,
                       sv=False, svpth=r"C:/Users/Travis W/Pictures/", svflnm='Unnamed',
                       cbl='Scale', vmin=None, vmax=None, cmap='viridis', cb=True, style='h'):
    """
    Overview
    ----------
    This program makes use of the ternary package and creates a ternary colormap

    Parameters
    ----------
    data: 4-tup of (a,b,c,i) where a, b, and c are the ternary coordinates and i is the intensity
    tertitle: chart title
    labelNames: Names of a, b, and c for chart axes
    scale: scale of chart (if 0-100, then scale is 100)
    sv: Boolean, save chart when true, show chart when false
    svpth: path to save ternary image
    svflnm: file name for ternary diagram when saving
    cbl: colorbar label
    vmin: minimum value of colorbar (leave blank to set to min value in i)
    vmax: maximum value of colorbar (leave blank to set to max value in i)
    cmap: determines color map used
    cb: use colorbar if true
    style: h = hexagons, d = triangles for point shape

    Returns
    -------

    """
    if sv:
        font = {'size': 12}   # Set font size for **kwargs
        figsize = (3.4, 2.5)
        ticksize = 6
        lnwdth = 0.5
        lnsty = '--'
        alpha = 0.15
    else:
        font = {'size': 30}   # Set font size for **kwargs
        figsize = (30, 30)
        ticksize = 20
        lnwdth = 2
        lnsty = ':'
        alpha = 0.5

    d = dict()
    x = data[:, 1]
    y = data[:, 0]
    if cb:
        i = data[:, 3]

        for col in range(1, len(x)):
            d[(x[col], y[col])] = i[col]
    else:
        for col in range(1, len(x)):
            d[(x[col], y[col])] = 0.5

    # Turn off normal axis, set figure size
    figure, ax = plt.subplots(figsize=figsize)
    ax.axis("off")

    # Create ternary axes (tax)
    figure, tax = ternary.figure(ax=ax, scale=scale)

    # Axis Labels (bottom corrisponds to x values, left corrisponds to y values)
    tax.bottom_axis_label(labelNames[1], offset=-0.1, **font)
    tax.left_axis_label(labelNames[2], offset=0.17, **font)
    tax.right_axis_label(labelNames[0], offset=0.17, **font)

    # Plot data, boundary, gridlines, and ticks
    tax.heatmap(d, style=style, cmap=cmap, cbarlabel=cbl, vmin=vmin, vmax=vmax, colorbar=cb)
    tax.boundary(linewidth=1)
    tax.gridlines(multiple=10, linewidth=lnwdth, alpha=alpha, linestyle=lnsty)
    ticks = [round(i / float(scale), 1) for i in range(0, scale+1, 10)]
    tax.ticks(ticks=ticks, axis='rlb', linewidth=1, clockwise=False, offset=0.03, textsize=ticksize)

    # Set chart title
    tax.set_title(tertitle)

    # Make chart pretty
    tax.clear_matplotlib_ticks()
    tax._redraw_labels()
    plt.tight_layout()

    # Save or show
    if sv:
        plt.savefig(''.join([svpth, svflnm]), dpi=600)
    else:
        tax.show()

def plt_tern_scatter(data, tertitle='',  labelNames=('Species A','Species B','Species C'), scale=100,
                       sv=False, svpth=r"C:/Users/Travis W/Pictures/", svflnm='Unnamed',
                       clr='k'):
    font = {'size': 24}

    # Turn off normal axis, set figure size
    figsize = [10,10]
    figure, ax = plt.subplots(figsize=figsize)
    ax.axis("off")

    figure, tax = ternary.figure(scale=scale)
    tax.set_title(tertitle, fontsize=20)
    tax.boundary(linewidth=2.0)
    tax.gridlines(multiple=10, color="k")

    # Axis Labels (bottom corrisponds to x values, left corrisponds to y values)
    tax.bottom_axis_label(labelNames[1], offset=0, **font)
    tax.left_axis_label(labelNames[2], offset=0.12, **font)
    tax.right_axis_label(labelNames[0], offset=0.12, **font)

    points = np.array([data[:,1], data[:,0]]).T

    # for WAXS MG stuff

    color = data[:, 3]
    print(color.shape)
    clrs = list()

    for i, col in enumerate(color):
        if col == 0:
            clrs.append('aqua')
        elif col == 1:
            clrs.append('lawngreen')
        else:
            clrs.append('yellow')
    # print(points, clrs)

    # end wax MG stuff

    tax.scatter(points, marker='o', color=clrs, s=100)
    tax.ticks(axis='lbr', linewidth=1, multiple=10, textsize=14)

    # Set chart title
    tax.set_title(tertitle)

    # Make chart pretty
    tax.clear_matplotlib_ticks()
    tax._redraw_labels()
    plt.tight_layout()
    plt.axis('off')

    if sv:
        plt.savefig(''.join([svpth, svflnm]), dpi=600)
    else:
        tax.show()
        
#
#data = np.genfromtxt('test_data.csv', delimiter=',')
##plt_ternary_save(data, tertitle='',  labelNames=('Co','Fe','V'), scale=100,
##                       sv=False, svpth=r"C:/Users/Travis W/Pictures/", svflnm='Unnamed',
##                       cbl='Scale', vmin=1, vmax=5, cmap='viridis', cb=True, style='h')
#
