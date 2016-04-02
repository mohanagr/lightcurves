#! /usr/bin/python3

import numpy as np

def prepareImage(image):
	var = image
	for i in range(1, 32): #leave the first row
		for j in range(0, 32):

			#replaces any NaN's with median value of pixel over the data cube (except the first row which is consistently bad)
			
			#nan = float('NaN')
			arr = var[:, i, j]
			arr[np.isnan(arr)] = np.nanmedian(var[:, i, j])
			var[:, i, j] = arr
			#np.place(var[:, i, j], var[:, i, j]==nan, np.nanmedian(var[:, i, j]))

	return var

# Additional operations on the image to be added here