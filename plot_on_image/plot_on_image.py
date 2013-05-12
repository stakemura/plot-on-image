# -*- coding:utf-8 -*-

"""
  @brief Plot 2D data on image using matplotlib
  @author Shintaro TAKEMURA (stakemura@gmail.com)
 
  This code is public domain, no warranty expressed or implied, 
  Functionality is thought to be correct, but it's up to you to make
  sure it does what you want.
"""

import os, sys
import re
import optparse
import csv
import urllib2
import logging; logger = logging.getLogger(__name__)

#import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def optdict(options, keys):
    return dict((k,getattr(options,k)) for k in keys if getattr(options,k)!=None)

if __name__ == '__main__':
    parser = optparse.OptionParser(version="0.02")
 
    parser.add_option("-i", dest="input_file", action='store',
                    metavar='FILE', help="input image file (required)")
    parser.add_option("-o", dest="output_file", action='store',
                    metavar='FILE', help="output image file (optional)")
    parser.add_option("--plot-points", dest="plot_points", action='store',
                    metavar='FILE', help="point data CSV file [(x,y)]")
    parser.add_option("--plot-contour", dest="plot_contour", action='store',
                    metavar='FILE', help="contour data CSV file [(x,y)]")
    parser.add_option("--plot-lines", dest="plot_lines", action='store',
                    metavar='FILE', help="line data CSV file [[(x,y)]]")
    parser.add_option("--plot-circles", dest="plot_circles", action='store',
                    metavar='FILE', help="circle data CSV file [(x,y,r)]")
    parser.add_option("--plot-polygons", dest="plot_polygons", action='store',
                    metavar='FILE',  help="polygon data CSV file [[(x,y)]]")
    parser.add_option("--delimiter", dest="delimiter", action='store', metavar='CHAR', default=',', help="CSV delimiter (default=comma)")
    parser.add_option("--fill", dest="fill", action='store_true', default=False, help="fill (default=false)")
    parser.add_option("--alpha", dest="alpha", metavar='FLOAT', action='store', help="alpha")
    parser.add_option("--color", dest="color", metavar='CHAR', action='store', help="color")
    parser.add_option("--facecolor", dest="facecolor", metavar='COLOR', action='store', help="face color")
    parser.add_option("--edgecolor", dest="edgecolor", metavar='COLOR', action='store', help="edge color")
    parser.add_option("--marker", dest="marker", metavar='MARKER', action='store', help="marker")
    parser.add_option("--markersize", dest="markersize", metavar='FLOAT', action='store', help="marker size")
    parser.add_option("--markerfacecolor", dest="markerfacecolor", metavar='COLOR', action='store', help="marker face color")
    parser.add_option("--markeredgecolor", dest="markeredgecolor", metavar='COLOR', action='store', help="marker edge color")
    parser.add_option("--markeredgewidth", dest="markeredgewidth", metavar='FLOAT', action='store', help="marker edge width")
    parser.add_option("--linewidth", dest="linewidth", metavar='FLOAT', action='store', help="line width")
    parser.add_option("--linestyle", dest="linestyle", metavar='STYLE',action='store', help="line style")
    parser.add_option("--hatch", dest="hatch", metavar='HATCH', action='store', help="hatch")
    parser.add_option("--dpi", dest="dpi", action='store', metavar='DPI', help="dots per inch")
    parser.add_option("--frameon", dest="frameon", action='store_true', default=False, help="figure frame")

    (options, args) = parser.parse_args()

    if not (options.input_file): 
        parser.print_help()
        sys.exit(-1)

    # create logger
    logger.setLevel(logging.DEBUG)
    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    # create formatter
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s %(message)s") 
    # add formatter to ch
    ch.setFormatter(formatter)
    # add ch to logger
    logger.addHandler(ch)

    # create a file-like object from the url
    # f=urllib2.urlopen("http://")

    # image to array
    img = mpimg.imread(options.input_file)
    plt.imshow(img)

    fig = plt.gcf()
    ax = fig.gca()

    if options.plot_points:
        with open(options.plot_points) as f:
            for row in csv.reader(f, delimiter=options.delimiter):
                x, y = map(float, row)
                ax.plot([x],[y], **optdict(options,
                        ['color', 'alpha', 'marker', 'markersize', 'markerfacecolor', 'markeredgecolor', 'markeredgewidth']))

    if options.plot_contour:
        with open(options.plot_contour) as f:
            pts = []
            for row in csv.reader(f, delimiter=options.delimiter):
                pts += map(float, row)
            ax.plot(pts[0::2]+[pts[0]], pts[1::2]+[pts[1]], **optdict(options,
                    ['color', 'alpha', 'marker', 'markersize', 'markerfacecolor', 'markeredgecolor', 'markeredgewidth', 'linewidth', 'linestyle']))

    if options.plot_lines:
        with open(options.plot_lines) as f:
            for row in csv.reader(f, delimiter=options.delimiter):
                pts = map(float, row)
                ax.add_artist(plt.Line2D(pts[0::2], pts[1::2], **optdict(options,
                              ['color', 'alpha', 'marker', 'markersize', 'markerfacecolor', 'markeredgecolor', 'markeredgewidth', 'linewidth', 'linestyle'])))

    if options.plot_circles:
        with open(options.plot_circles) as f:
            for row in csv.reader(f, delimiter=options.delimiter):
                x, y, r = map(float, row)
                ax.add_artist(plt.Circle((x,y), r, **optdict(options,
                              ['color', 'alpha', 'fill', 'facecolor', 'edgecolor', 'linewidth', 'linestyle', 'hatch'])))

    if options.plot_polygons:
        with open(options.plot_polygons) as f:
            for row in csv.reader(f, delimiter=options.delimiter):
                pts = map(float, row)
                ax.add_artist(plt.Polygon(zip(pts[0::2],pts[1::2]), **optdict(options,
                              ['color', 'alpha', 'fill', 'facecolor', 'edgecolor', 'linewidth', 'linestyle', 'hatch'])))

    if options.output_file:
        plt.savefig(options.output_file, dpi=options.dpi, frameon=options.frameon, transparent=True)
    else:
        plt.show()
