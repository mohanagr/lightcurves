#! /usr/bin/python3

import subprocess

def check():
	packages = ['astropy', 'matplotlib', 'numpy']
	for package in packages:
		try:
			return __import__(package)
		except ImportError:
			subprocess.run("pip3 install {}".format(package), shell=True)
			return None

if __name__ == "__main__": 
	check()
	print('Setup complete')

