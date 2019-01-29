#Plotting Sea Level Anomalies from the Bermuda dataset with a Hovmoller diagram
from netCDF4 import Dataset #Needed to import dataset
import matplotlib.pyplot as plt #importi matplotlib.pyplot
import numpy as np #import numpy with the nickname of np
dataset = Dataset("/Users/student/Desktop/BridgeUP-STEM-Abbott/datasets/Bermuda_data_SLA.nc")
dataset.ncattrs()
#Defining the variables lat=latitude
#long = longitutude;sla = sea level anomaly;time= time
lat = dataset.variables['latitude']
long = dataset.variables['longitude']
sla = dataset.variables['sla'][:]


dataset.variables.keys()
time = dataset.variables['time']
graph = plt.pcolor(long[:], lat[:], sla[:,:,0], cmap='cubehelix')
cb = plt.colorbar(graph)
time = dataset.variables['time']
graph = plt.pcolor(long[:], time[:], sla[:,0,:], cmap='cubehelix')
cb = plt.colorbar(graph)
cb.set_label('m')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Sea level Anomalies in Bermuda on day 9149')
#plt.savefig('SLA Bermuda 9149', format = 'png', dpi=1000)
long
long.shape
time.shape
sla.shape
sla[:,0,:]
#sla[:,:,0]
sla.data
plt.pcolor(time[:],lat[:],sla[:,:,0].T, cmap='cubehelix')

#hovmoller forloop
import datatime
time.data
dates = []

for day in time:
    newdays = datetime.date(month=1, day=1, year=1950) + datetime.timedelta(day + 0)
    date

day = time[0]
day

day + 0
newdays = datetime.date(month=1, day = 1, year = 1950) + datetime.timedelta(day + 0)

newdays
