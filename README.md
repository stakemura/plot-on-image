plot-on-image
===================
Plot 2D data on image using matplotlib


Requirement
-----------
* Python 2.6 or later
* [matplotlib](http://matplotlib.org/) 1.2 or later

How to use
----------
	Usage: plot_on_image.py [options]

	Options:
	  --version             show program's version number and exit
	  -h, --help            show this help message and exit
	  -i FILE               input image file (required)
	  -o FILE               output image file (optional)
	  --plot-points=FILE    points data file [(x,y)]
	  --plot-circuit=FILE   closed path data file [(x,y)]
	  --plot-lines=FILE     lines data file [[(x,y)]]
	  --plot-circles=FILE   circles data file [(x,y,r)]
	  --plot-polygons=FILE  polygons data file [[(x,y)]]
	  --delimiter=CHAR      CSV delimiter (default=comma)
	  --fill                fill (default=false)
	  --alpha=FLOAT         alpha
	  --color=CHAR          color
	  --facecolor=COLOR     face color
	  --edgecolor=COLOR     edge color
	  --marker=MARKER       marker
	  --markersize=FLOAT    marker size
	  --markerfacecolor=COLOR
	                        marker face color
	  --markeredgecolor=COLOR
	                        marker edge color
	  --markeredgewidth=FLOAT
	                        marker edge width
	  --linewidth=FLOAT     line width
	  --linestyle=STYLE     line style
	  --hatch=HATCH         hatch
	  --dpi=DPI             dots/inch for output image
	  --frameon             figure frame for output image

Sample
------
	python -i background.png --plot-points points.csv --marker=x --color=orange --linewidth=2 --markeredgecolor=red --markeredgewidth=1

License
------
public domain
