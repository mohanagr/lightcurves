# lightcurves

> A basic lightcurve generator for images obtained from IRAC instrument of SPITZER space telescope.

The program deals with [dot]fits files. IRAC captures multiple frames at a time gap specified by 'FRAMTIM' header of the fits file (usually 2 seconds). Each fits file consists of 32 x 32 frames, 64 in number. The lightcurve has been plotted between the intensity of the brightest pixel in the frame vs the time elapsed. (First frame is captured at t = 0 seconds). 

## Setup
1. Clone this repository and make it the current working directory.
2. Make sure pip3 is installed.
3. Run setup.py
4. The Program can now be run by - ``./lightcurve.py ./Samples/r46467072/ch2/bcd`` Replace ``./Samples/r46467072/ch2/bcd`` with the path to the directory containing fits images for which lightcurve is to be plotted.
5. After successfully running the program the output is stored in ``\home\username\outputs\``

## Samples
All samples have been obtained from the Spitzer Heritage archive - http://sha.ipac.caltech.edu/applications/Spitzer/SHA/
The samples included herewith are specifically a part of the real observations of the transiting hot Jupiter XO-3b passing behind its host star. (The folder names in ``Samples`` are the AORKEYS of the observation). 
For details refer http://irachpp.spitzer.caltech.edu/page/data-challenge-2015
