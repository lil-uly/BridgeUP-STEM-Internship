##Plotting sea level anomaly from netCDF4 Dataset##
#


from netCDF4 import Dataset #importing library tool, NECESSARY Tool we need to load in our nc dataset
import numpy as np
import matplotlib.pyplot as plt
dataset = Dataset("/Users/student/Desktop/BridgeUP-STEM-Oceans-Six/datasets/Bermuda_data_SLA.nc") #creating a variable, NECESSARY

dataset.ncattrs() #tells me about the metadata of my dataset, COOL
print(dataset.variables)
dataset.variables.keys() #keys: the specific data variables we're working with

#dataset.variables['sla'][:].shape #selecting the size of the (3d) array for our variable.
dataset.variables['time'][:].shape

lat = dataset.variables['latitude']
lon = dataset.variables['longitude']
sla = dataset.variables['sla']
time = dataset.variables['time']

graph = plt.pcolor(lat[:], time[:], sla[:,:,0], cmap='Spectral_r')
cb = plt.colorbar(graph)
cb.set_label('m')
plt.xlabel('latitude')
plt.ylabel('time')
plt.title('Sea Level Anomaly in Bermuda (hovmoller diagram)')
plt.savefig('SLA_Bermuda_9149_Hovmoller.png', format = 'png', dpi = 1000)

def sla_plot(day):
    graph = plt.pcolor(lon[:], lat[:], sla[day,:,:], cmap ='plasma')
    cb = plt.colorbar(graph) #adding in our data into the colorbar(key/legend)
    cb.set_label('m')
    plt.xlabel('longitude')
    plt.ylabel('latitude')
    plt.title('Sea level anomaly in Bermuda on day {}'.format(day))


sla_plot(10)
def plot_loop(day):
    for i in range(day):
        fig = plt.figure()
        graph = plt.pcolor(lon[:], lat[:], sla[i,:,:], cmap ='cubehelix')
        cb = plt.colorbar(graph)
        cb.set_label('m')
        plt.xlabel('longitude')
        plt.ylabel('latitude')
        plt.title('Sea level anomaly in Bermuda on day {}'.format(i))
