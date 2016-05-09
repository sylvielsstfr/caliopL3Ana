# caliopL3Ana
===============

Creation Thu 21 April 2016
Update 9 May 2016


This is my first work on CALIOP (Callipso) data.
I wrote an ipython notebook to explore the data:

These data are summary 2 x 12 files, of L3 level converted from hdf to h5.

- one file per month
- one file for days, one file for nights


## The analysis is avaialble in the following ipython notebook:
==============================================================


### all ipython notebook
AstroObservLocation.ipynb		ScanAerosolsOneYear_v1.ipynb
AtmProperties1Year.ipynb		ScanAerosolsOneYear_v2.ipynb
ExploreL3Aerosolsv0.ipynb		ScanAerosolsTenYears.ipynb
ExploreL3Data-Copy1.ipynb		ScanManyAerosolMapsOneYear.ipynb
ExploreL3Datav0.ipynb			ScanManyAerosolMapsSAOneYear.ipynb
ExploreL3Datav1.ipynb			ShowGranules.ipynb
ScanAerosolMapsOneYear.ipynb		example_histowithdates.ipynb
ScanAerosolsOneYear.ipynb


### library

libCaliopAOD.py




### Example to explore data (21 April 2016)
=========================================
- ExploreL3Data-Copy1.ipynb
- ExploreL3Datav0.ipynb
- ExploreL3Datav1.ipynb

### Go further with the aerosols, especially looking at different types of aerosols (22 April 2016):
=====================================================================================================

- ExploreL3Aerosolsv0.ipynb
- ExploreL3Datav1.ipynb		

It shows the rise of aerosols when the construction has started.


### shows otherthan AOD quantities above LSST site 



### Scan One year of aerosols and plot AOD vs month (22 April 2016)
===================================================================

Aerosols at LSST site longtitude-latitude bin.

- ScanAerosolsOneYear.ipynb
- AerosolsOneYear_v1.ipynb show a nicer plot 
- ScanAerosolsOneYear_v2.ipynb

under devoloppement for 10 years
- ScanAerosolsTenYears.ipynb

### Show maps of AOD

- AOD world map for one year		
- ScanManyAerosolMapsOneYear.ipynb
- AOD map above South America
- ScanManyAerosolMapsSAOneYear.ipynb


### other quantities than AOD
- AtmProperties1Year.ipynb







## Some plots have been saved in /plot directory
================================================


## The list of inut files:
L3 Data from Calipso.
Those are monthly averaged data according night and day périod.
Here we took a data selection called AllSky-Standard.



- CAL_LID_L3_APro_AllSky-Standard-V3-00.2013-01D.h5
- CAL_LID_L3_APro_AllSky-Standard-V3-00.2013-01N.h5
- CAL_LID_L3_APro_AllSky-Standard-V3-00.2013-02D.h5
- CAL_LID_L3_APro_AllSky-Standard-V3-00.2013-02N.h5
- CAL_LID_L3_APro_AllSky-Standard-V3-00.2013-03D.h5
- CAL_LID_L3_APro_AllSky-Standard-V3-00.2013-03N.h5
- CAL_LID_L3_APro_AllSky-Standard-V3-00.2013-04D.h5
- CAL_LID_L3_APro_AllSky-Standard-V3-00.2013-04N.h5
- CAL_LID_L3_APro_AllSky-Standard-V3-00.2013-05D.h5
- CAL_LID_L3_APro_AllSky-Standard-V3-00.2013-05N.h5
- CAL_LID_L3_APro_AllSky-Standard-V3-00.2013-06D.h5
- CAL_LID_L3_APro_AllSky-Standard-V3-00.2013-06N.h5
- CAL_LID_L3_APro_AllSky-Standard-V3-00.2013-07D.h5
- CAL_LID_L3_APro_AllSky-Standard-V3-00.2013-07N.h5
- CAL_LID_L3_APro_AllSky-Standard-V3-00.2013-08D.h5
- CAL_LID_L3_APro_AllSky-Standard-V3-00.2013-08N.h5
- CAL_LID_L3_APro_AllSky-Standard-V3-00.2013-09D.h5
- CAL_LID_L3_APro_AllSky-Standard-V3-00.2013-09N.h5
- CAL_LID_L3_APro_AllSky-Standard-V3-00.2013-10D.h5
- CAL_LID_L3_APro_AllSky-Standard-V3-00.2013-10N.h5
- CAL_LID_L3_APro_AllSky-Standard-V3-00.2013-11D.h5
- CAL_LID_L3_APro_AllSky-Standard-V3-00.2013-11N.h5
- CAL_LID_L3_APro_AllSky-Standard-V3-00.2013-12D.h5
- CAL_LID_L3_APro_AllSky-Standard-V3-00.2013-12N.h5


To make a push do:

> git remote set-url origin git@github.com:sylvielsstfr/caliopL3Ana.git
> git push origin master

