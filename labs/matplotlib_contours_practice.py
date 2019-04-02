## Put your import statements here.
## What packages do you want to import?
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
%matplotlib inline
from netCDF4 import Dataset
import datetime
## practice
lat = [32, 32.2, 32.4, 32.6, 32.8, 33., 33.2, 33.4, 33.6, 33.8, 34.]
lon = [294, 294.2, 294.4, 294.6, 294.8, 295, 295.2, 295.4, 295.6, 295.8, 296]
sla = np.random.randn(11,11)

### Challenge 1
## Given the above latitudes, longitudes and sea level anomaly
## grid, do the following:
    #A) Make a contour plot of the sla dataset
    #B) Make a filled in contour plot, and add a colorbar
    #C) Create custom levels for the contour plot that are
    # evenly spaced at 0.25 meters apart and cover the entire range of sla
    # (i.e.) there are contour lines even at the max/min heights
    #hint: np.arange may help with this: https://www.sharpsightlabs.com/blog/numpy-arange/
    #D) save your plots to your repository
    #E) How many "eddies" do you see?


####Challenge 1
#Challenege 1a
xlist = np.linspace(290, 300, 10)#longitude
ylist = np.linspace(30, 35, 5)#latitude
zlist = sla
X, Y = np.meshgrid(xlist, ylist)
plt.contour(lon, lat, sla)
#Challenege 1b

#Challenege 1c
levels =(np.arange(start=-2, stop=2,step=0.25))
plt.figure()
plt.contourf(lon, lat, sla, levels)

### Challenge 2
## Load in our dataset of SLA in Bermuda, and repeat
## exercises A-E for the entire dataset region. Pick a single day
## of SLA.

##Day Index

def date_adder(day):
    return datetime.date(month = 1,day = 1, year = 1950) + datetime.timedelta(int(day))


dataset = Dataset("/Users/student/Desktop/BridgeUP-STEM-Abbott/datasets/Bermuda_data_SLA.nc")
lati = dataset.variables['latitude'][:]
long = dataset.variables['longitude'][:]
sla_data = dataset.variables['sla'][:]
time = dataset.variables['time'][:]
long_min= (np.min(long))
long_max= (np.max(long))
lati_min= (np.min(lati))
lati_max= (np.max(lati))

zlist_sla = sla_data[0]
X, Y = np.meshgrid(xlist_long, ylist_lati)
plt.title('Sea level anomaly in Bermuda on day {}'.format(date_adder(time[9148])))
plt.contourf(long, lati, sla_data[9148])

#Challenege 1c
print(np.arange(start=-2, stop=2,step=0.25))

## Bonus points if you make the day index a variable (like
## our plotting function) so you can easily change it to see different

## contour maps for different days
