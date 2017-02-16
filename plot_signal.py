import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import scale
from scipy.interpolate import interp1d

'''
Author: Federico Terzi
This is a work in progress, don't judge please :)
'''

filename = "a_sample_11.txt"
sample_size_fit = 50

data_raw = [map(lambda x: int(x), i.split(" ")[1:-1]) for i in open(filename)]

data = np.array(data_raw)

data_norm = scale(data)

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

plt.plot(acx_stretch)
plt.plot(acy_stretch)
plt.plot(acz_stretch)

plt.plot(gx_stretch)
plt.plot(gy_stretch)
plt.plot(gz_stretch)

plt.show()

print data
print data_norm