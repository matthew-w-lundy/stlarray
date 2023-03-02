from astropy.io import fits
from astropy.utils.data import get_pkg_data_filename

import numpy as np
from stlarray.array2stl import makestl

image_file = get_pkg_data_filename('tutorials/FITS-images/HorseHead.fits')
image_data = fits.getdata(image_file, ext=0)

rowbin=5
colbin=5

image_data=image_data[:(np.shape(image_data)[0]//rowbin)*rowbin,:(np.shape(image_data)[0]//colbin)*colbin]

rebin=image_data.reshape(np.shape(image_data)[0]//rowbin,rowbin,np.shape(image_data)[1]//colbin,colbin)

rebin=rebin.mean(axis=3).mean(axis=1)


makestl(rebin,filename='horseshoe_interp.stl',method='interp')
