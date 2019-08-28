from netCDF4 import Dataset #Importing Library Tool, NECESSARY 
 dataset = Dataset('/Users/student/Desktop/BridgeUP-STEM-Abbott/datasets/sea_surface_temp.nc')
   #Creating a variable called dataset which is used to call to the dataset being used 
dataset.ncattrs() #cCool but not necessary 