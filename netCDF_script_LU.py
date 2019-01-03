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
sla
dataset.variables.keys()
time = dataset.variables['time']
graph = plt.pcolor(long[:], lat[:], sla[0,:,:], cmap='cubehelix')
cb = plt.colorbar(graph)
time = dataset.variables['time']
graph = plt.pcolor(long[:], lat[:], sla[9148,:,:], cmap='cubehelix')
cb = plt.colorbar(graph)
cb.set_label('m')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Sea level Anomalies in Bermuda on day 9149')
plt.savefig('SLA Bermuda 9149', format = 'png', dpi=1000)
lat.shape
long.shape
sla.shape
