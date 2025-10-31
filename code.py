import healpy as hp
import numpy as np
import matplotlib.pyplot as plt


#loading the kids mask
#each pixel = value describing coverage/weight (0 = empty, >0 = observed e.g.) 
KIDS_MASK_PATH = "/share/data1/xzcapsad/des_kids/kids_dr4//K1000_healpix_DR4.1_nside_4096.fits" 

#returns a 1D numpy array - each element corresponds to a pixel on the sphere
#mask shape = (12*nside^2,)
#entry gives a weight/number of exposures for that sky pixel
mask = hp.read_map(KIDS_MASK_PATH)
#HEALPix resolution parameter = how finely the sphere is pixelated 
#number of pixels - npix = 12 * nside^2
nside = hp.get_nside(mask)
#area of each pixel in square degrees
#for converting pixel counts to sky area
pixarea_deg2 = hp.nside2pixarea(nside, degrees=True)

#printing stats 
#mask.size - number of pixels in the mask
#mask.min()/max() - min/max values in the mask - 0-80? for kids 
print(nside)
#number of pixels that are nonzero =  covered by survey footprint
print('Mask values - min, max, nonzero count:',
      float(mask.min()), float(mask.max()), int(np.count_nonzero(mask)))

#calculating sky areas
#mask > 0 : boolean array: True where covered, False elsewhere
#np.sum = number of pixels within the footprint
#Multiplying by the area of one pixel = total area in square degrees
area_kids_deg2 = np.sum(mask > 0) * pixarea_deg2

#showing the mask
hp.mollview(mask, title="KiDS mask")
plt.show()

plt.savefig("kids_mask.png")