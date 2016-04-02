#! /usr/bin/python3

import numpy as np
import sys
import os
import fnmatch
from astropy.io import fits
from Modules import prepareImage as prep_img
from Modules import plotcurve as plot


def main():
	path = sys.argv[1]
	for file in os.listdir(path):

		# Check if there's a bcd.fits file in the given path
		if fnmatch.fnmatch(file, '*bcd.fits'):
			fpath = path+'/'+file
			filename = file.split('.')[0]
			
			hdulist = fits.open(fpath)
			imgdata = hdulist[0].data
			prihdr = hdulist[0].header
			frametime = prihdr['FRAMTIME']  # Time difference between two frames
			
			# Edit Image
			final = prep_img.prepareImage(imgdata)
			
			# Find the brightest pixel in a frame 
			im0 = final[0, :, :]
			i, j = np.unravel_index(np.nanargmax(im0), im0.shape) 
			maxval = np.nanmax(final[:, i, j]);
			minval = np.nanmin(final[:, i, j]);
			
			# Plot the lightcurve and save the output
			plot.plotcurve(final, frametime, i, j, filename, minval, maxval)
			



if __name__ == "__main__": main()




