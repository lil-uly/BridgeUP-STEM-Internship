## Put any import statements here
from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
import datetime
import pandas as pd


## Load in our Bermuda SLA dataset here.

dataset = Dataset("/Users/student/Desktop/BridgeUP-STEM-Abbott/datasets/Bermuda_data_SLA.nc")

lat=dataset.variables["latitude"][:]
long=dataset.variables["longitude"][:]

time=dataset.variables["time"][:]

sla=dataset.variables['sla'][:]

long_min=(np.min(long))
long_max=(np.max(long))
lat_min=(np.min(lat))
lat_max= (np.max(lat))
sla_min = (np.min(sla))
sla_max = (np.max(sla))


## Make a contour plot of a single day of sea level anomaly data here.
## Make sure to save the contour plot as a variable!
## Use levels that are spaced evenly every 0.01 meters (this is the units of SLA)

##Assigns the date to the corresponding day of data
day = 0
def date_adder(day):
  return datetime.date(year=1950, month=1, day=1) + datetime.timedelta(int(day))

mmddyy=[]
##Unsuccessful attempt at converting days to dates

'''for value in time:
   converted_dates=date_adder(value)
   mmddyy.append(converted_dates)'''

  #Defines the contours for each day
def contour (day):
   long_min=(np.min(long))
   long_max=(np.max(long))
   lat_min=(np.min(lat))
   lat_max= (np.max(lat))

   Z= sla[day]
   X, Y = np.meshgrid(long, lat)

   cp = plt.contourf(long, lat, sla[day])
   plt.colorbar(cp)
   plt.xlabel ('longitude')
   plt.ylabel('latitude')
   plt.title(" Contour Sea Level Anomaly Plot for Bermuda on {}".format(mmddyy[day]))
   #plt.savefig("Contour Sea Level Anomaly Plot for Bermuda on {}".format(mmddyy[day]))

##Plots contour plot with filled data
cp = plt.contourf(long, lat, sla[day])



## Write a function that takes in a contour plot object and an index and
## returns the level value at that index and a list containing all of the Path objects
## for that level. (all of the contour lines that share that level value)

#Says the level for the day and the vertices connecting the level
def coordinate1(day, level):
    print("The current level is:")
    print(level)
    print(cp.collections[day].get_paths()[level].vertices)

coordinate1(3, 2)


cp = plt.contour(long, lat, sla[day])


#Returns contour paths for each level
def contour_levels(level):
    return cp.collections[level].get_paths()

#Defines the coordinates of each level
def coordinates(level):
   levels= np.arange(start=sla_min,stop=sla_max, step=0.01)
   a=(levels[level])
   b=(cp.collections[level].get_paths())
   return a,b

#Different levels for each contour
levels= np.arange(start=sla_min,stop=sla_max, step=0.01)



sla_list = np.arange(sla_min, sla_max, 0.01)




## Write code to create a Pandas dataframe where each contour line and
## corresponding level is stored as an individual row.
## There are many ways you can do this. The goal is a dataframe that looks like:

#sla_list = cp.levels
 ##Converting the list to a table
 #First attempt for DataFrame - Failure
'''for counter, value in enumerate(sla_list):
    print(counter, value)

def df_creator(value):
    for value in sla
        dataframe = pd.DataFrame({'LEVEL': cp.levels[], 'PATH': cp.collections[3].get_paths() })'''

#Successful Attempt for Pandas Dataframe
df = pd.DataFrame()
for item in range(0, len(cp.levels)):
   level,paths= coordinates(item)
   df1= pd.DataFrame({'LEVEL': level, 'PATH': paths})
   df=df.append(df1, ignore_index=True)

print(df)



###Algorithm for Contour Levels
##If contour levels are open, drop the contour line
