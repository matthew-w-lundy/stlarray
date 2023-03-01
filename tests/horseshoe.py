from astropy.io import fits
from astropy.utils.data import get_pkg_data_filename

import numpy as np
from stlarray.array2stl import makestl

image_file = get_pkg_data_filename('tutorials/FITS-images/HorseHead.fits')
image_data = fits.getdata(image_file, ext=0)



makestl(image_data[::10,::10],filename='horseshoe.stl')
