from netCDF4 import Dataset #Tool we need to load in our nc dataset
import numpy as np
import matplotlib.pyplot as plt
dataset = Dataset('/Users/student/Desktop/BridgeUP-STEM-Abbott/datasets/Bermuda_data_SLA.nc')  #Loading in our dataset

print(dataset.variables)
dataset.variables.keys()


dataset.variables['sla'][:].shape
dataset.variables['time'][:].shape

lat = dataset.variables['latitude']
lon = dataset.variables['longitude']
sla = dataset.variables['sla']
time= dataset.variables['time']
time[:]


graph = plt.pcolor(lon[:], lat[:], sla[day,:,:], cmap ='plasma')
cb = plt.colorbar(graph)
cb.set_label('m')
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.title('Sea level anomaly in Bermuda on day 9149')
#plt.savefig('sla_Bermuda_9149.png', format = 'png', dpi = 1000)


#Plots chart day by day




import datetime
def date_adder(day):
    return datetime.date(month = 1,day = 1, year = 1950) + datetime.timedelta(int(day))


date_adder(9140)

mmddyy = []

'''for dates in time:
    mmddyy.append(date_adder(dates))
    print(mmddyy)'''


def sla_plot(day):
    graph = plt.pcolor(lon[:], lat[:], sla[day,:,:], cmap ='Purples')
    cb = plt.colorbar(graph)
    cb.set_label('m')
    plt.xlabel('longitude')
    plt.ylabel('latitude')
    plt.title('Sea level anomaly in Bermuda on day {}'.format(date_adder(time[day])))
    plt.savefig('SLA_Bermuda_day{}'.format(date_adder(time[day])))

sla_plot(3651)

day
#2002 day range: 3287 - 3652
for d in range(3651,3652):
        fig = plt.figure(figsize=(8,5))
        graph = plt.pcolor(lon[:], lat[:], sla[d,:,:], cmap ="Spectral")
        cb = plt.colorbar(graph)
        cb.set_label('m')
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.title('Sea level anomaly in Bermuda on day {}'.format(date_adder(time[d])))
        plt.savefig('SLA_Bermuda_day{}'.format(date_adder(time[d])))

for d in range(3287,3651):
        fig = plt.figure(figsize=(8,5))
        graph = plt.pcolor(lon[:], lat[:], sla[d,:,:], cmap ='Spectral')
        cb = plt.colorbar(graph)
        cb.set_label('m')
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.title('Sea level anomaly in Bermuda on day {}'.format(date_adder(time[d])))
        plt.savefig('Timelapse/SLA_Bermuda_day{}.png'.format(d),format="png",dpis=500)

#Calculating the number of days needed
2002 - 1993
9 * 365
3287 + 365
