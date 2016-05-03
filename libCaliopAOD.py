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



    
#--------------------------------------------------------------------------------
def GetL3FilenameDay(path,base,year,month):
    month_str='%02d' % (month+1)
    fullpath_root=os.path.join(os.path.join(path,str(year)),'hdf5')
    dayfile_extension= str(year)+'-'+month_str+'D.h5'  
    dayfile_fullname=os.path.join(fullpath_root,base+'.'+dayfile_extension)
    return dayfile_fullname
#---------------------------------------------------------------------------------    
    
#--------------------------------------------------------------------------------    
def GetL3FilenameNight(path,base,year,month):
    month_str=str('%02d' % (month+1))
    fullpath_root=os.path.join(os.path.join(path,str(year)),'hdf5')
    nightfile_extension= str(year)+'-'+month_str+'N.h5'  
    nightfile_fullname=os.path.join(fullpath_root,base+'.'+nightfile_extension)
    return nightfile_fullname
#-------------------------------------------------------------------------------    


#-------------------------------------------------------------------------------
def GetL3Value(filename,keyname,lat=Latitude_lsst,long=Longitude_lsst):
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
#-------------------------------------------------------------------------------    

#--------------------------------------------------------------------------------
def GetL2APAltitudes():
    # Generate altitude data according to file specification [1].

    bin_layer1=290
    bin_layer2=200
    bin_layer3=55
    

    #alt = np.zeros(290)
    alt = np.zeros(bin_layer1+bin_layer2+bin_layer3)

    # You can visualize other blocks by changing subset parameters.
    #  20.2km to 30.1km
    # for i in range (0, 54):
    #       alt[i] = 20.2 + i*0.18;
    for i in range(0,bin_layer3):
       alt[i+bin_layer1+bin_layer2-1] = 20.2 + i*0.18;

    #  8.2km to 20.2km
    # for i in range (0, 199):
    #       alt[i] = 8.2 + i*0.06;
    for i in range(0,bin_layer2-1):
        alt[i+bin_layer1] = 8.2 + i*0.06;

    # -0.5km to 8.2km
    #for i in range (0, 289):
    for i in range (0, bin_layer1):
          alt[i] = -0.5 + i*0.03
                           
    return alt
#---------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
def GetL3APAltitudes():
    # Generate altitude data according to file specification 
    # CALIPSO Data management and Data product 

    bin_layer=208
    alt = np.zeros(bin_layer)
    
    # -0.4km to 12.1 km
    #for i in range (0, 289):
    for i in range (0, bin_layer):
        alt[i] = -0.4 + i*0.06
                           
    return alt
#--------------------------------------------------------------------------------    

if __name__ == "__main__":

    # If a certain environment variable is set, look there for the input
    # file, otherwise look in the current directory.

    # defines a few constants
    year=2015
    month=0
    path_root='/Users/dagoret-campagnesylvie/MacOsX/LSST/MyWork/CALIPSO/DATA/ICARE/CALIOP/L3/CAL_LID_L3_APro_AllSky.v3.00/CAL_LID_L3_APro_AllSky.v3.00'
    filename_base='CAL_LID_L3_APro_AllSky-Standard-V3-00'
  
    dayfile_fullname=GetL3FilenameDay(path_root,filename_base,year,month)
    nightfile_fullname=GetL3FilenameNight(path_root,filename_base,year,month)
    
    print "FILE = ",dayfile_fullname
    
    print GetL3Value(dayfile_fullname,'AOD_Mean')
    print GetL3Value(nightfile_fullname,'Relative_Humidity_Mean')
    print GetL3Value(dayfile_fullname,'Temperature_Mean')
    print GetL3Value(dayfile_fullname,'Pressure_Mean')
    print GetL3APAltitudes() 
    
    plt.plot(GetL3APAltitudes())
    