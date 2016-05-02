# -*- coding: utf-8 -*-
"""
Created on Mon May  2 19:28:37 2016

libCaliopAOD

Library to extract data from L3 Calipso hdf5 files.

@author: dagoret-campagnesylvie
"""

import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap
from matplotlib import colors
import h5py

#LSST site
Longitude_lsst = -70.7366833333333 # deg
Latitude_lsst = -30.240741666666672 #deg
Altitude_lsst = 2749.999999999238 #m

def GetValue(filename,keyname,lat=Latitude_lsst,long=Longitude_lsst):
    h5f = h5py.File(filename, "r")  # file on which one works
    # table of longitudes
    longitude=h5f['Longitude_Midpoint']   # shape =(1,72)
    all_longitude=longitude[0,:]    # coordinates for X
    # table of latitudes
    latitude=h5f['Latitude_Midpoint']     # shape = (1,85)
    all_latitude=latitude[0,:]      # coordinate for Y
    # which pixel correspond to the long lat
    long_indexes=np.where(np.logical_and(all_longitude>=long-2.5, all_longitude<=long+2.5))
    lat_indexes=np.where(np.logical_and(all_latitude>=lat-1, all_latitude<=lat+1))
    lat_index=lat_indexes[0]
    long_index=long_indexes[0]
    data_array=h5f[keyname]
    #h5f.close()
    return data_array[lat_index,long_index] 
    



if __name__ == "__main__":

    # If a certain environment variable is set, look there for the input
    # file, otherwise look in the current directory.

    # defines a few constants
    year=2015
    month=0
    
    month_stringnumber=['01','02','03','04','05','06','07','08','09','10','11','12']
    path_root='/Users/dagoret-campagnesylvie/MacOsX/LSST/MyWork/CALIPSO/DATA/ICARE/CALIOP/L3/CAL_LID_L3_APro_AllSky.v3.00/CAL_LID_L3_APro_AllSky.v3.00'
    fullpath_root=os.path.join(os.path.join(path_root,str(year)),'hdf5')
    filename_base='CAL_LID_L3_APro_AllSky-Standard-V3-00'
    
    dayfile_extension= str(year)+'-'+month_stringnumber[month]+'D'+'.h5'
    nightfile_extension=str(year)+'-'+month_stringnumber[month]+'N'+'.h5'
    dayfile_fullname=os.path.join(fullpath_root,filename_base+'.'+dayfile_extension)
    nightfile_fullname=os.path.join(fullpath_root,filename_base+'.'+nightfile_extension)
    
    print GetValue(dayfile_fullname,'AOD_Mean')
    print GetValue(dayfile_fullname,'Relative_Humidity_Mean')
    print GetValue(dayfile_fullname,'Temperature_Mean')
    print GetValue(dayfile_fullname,'Pressure_Mean')
    