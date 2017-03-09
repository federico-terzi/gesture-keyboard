import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import scale
from scipy.interpolate import interp1d
import sys

'''
Author: Federico Terzi

This module simply plots a signal.

You can specify the signal filename as a parameter in the terminal.

This is a work in progress...
'''

ALL_AXES=False

filename = sys.argv[1]
sample_size_fit = 50

data_raw = [map(lambda x: int(x), i.split(" ")[1:-1]) for i in open(filename)]

data = np.array(data_raw).astype(float)

f, axarr = plt.subplots(3)

axarr[0].set_title("Raw Data")
if ALL_AXES:
	axarr[0].plot(data)
else:
	axarr[0].plot(data[:,1])

#print data

data_norm = scale(data)

axarr[1].set_title("Y Normalized Data")
if ALL_AXES:
	axarr[1].plot(data_norm)
else:
	axarr[1].plot(data_norm[:,1])

acx = data_norm[:,0]
acy = data_norm[:,1]
acz = data_norm[:,2]

gx = data_norm[:,3]
gy = data_norm[:,4]
gz = data_norm[:,5]

x = np.linspace(0, data.shape[0], data.shape[0])
f_acx = interp1d(x, acx)
f_acy = interp1d(x, acy)
f_acz = interp1d(x, acz)

f_gx = interp1d(x, gx)
f_gy = interp1d(x, gy)
f_gz = interp1d(x, gz)

xnew = np.linspace(0, data.shape[0], sample_size_fit)

acx_stretch = f_acx(xnew)
acy_stretch = f_acy(xnew)
acz_stretch = f_acz(xnew)

gx_stretch = f_gx(xnew)
gy_stretch = f_gy(xnew)
gz_stretch = f_gz(xnew)


axarr[2].set_title("X Normalized to 50 samples")
axarr[2].plot(acx_stretch)
if ALL_AXES:
	axarr[2].plot(acy_stretch)
	axarr[2].plot(acz_stretch)

	axarr[2].plot(gx_stretch)
	axarr[2].plot(gy_stretch)
	axarr[2].plot(gz_stretch)

plt.show()

# print data
# print data_norm