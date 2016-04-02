#! /usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import os.path
from os.path import expanduser


def plotcurve(image, frametime, pixel_x, pixel_y, filename, ymin, ymax):  

	# Create an output folder to store the images if it doesn't already exist
	home = expanduser("~") # cross-platform
	directory = home+'/output'
	if not os.path.exists(directory):
		os.makedirs(directory)
		
	# Plot the lightcurve
	t = np.arange(0, 128, frametime)
	plt.plot(t, image[:, pixel_x, pixel_y], 'r--')
	plt.axis([0, 128, ymin-10, ymax+10])
	plt.xlabel('Time in sec')
	plt.ylabel('Flux in MJy/sr')

	# Save to the target directory and close
	plt.savefig(directory+'/'+filename+'_lightcurve.png')
	plt.close()