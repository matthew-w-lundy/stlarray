from astropy.io import fits
import numpy as np
from stlarray.array2stl import makestl
filepath="/home/matthew/MGRUO/crabtest/"
hdul = fits.open(filepath+"/results__s6.fits")
data=hdul[6].data




makestl(np.nan_to_num(data),filename='crab.stl')
