from netCDF4 import Dataset

dataset = Dataset("/Users/student/Desktop/BridgeUP-STEM-Abbott/datasets/Bermuda_data_SLA.nc")
print("Liliann")

print(dataset)
print(Dataset.variables)
dataset.ncattrs()
dataset.geospatial_lat_min
dataset.geospatial_lat_max
dataset.geospatial_lon_min
dataset.variables['latitude'][:]
dataset.variables['sla'][:]
dataset.variables["longitude"][:]
