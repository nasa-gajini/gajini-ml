import xarray as xr
import matplotlib.pyplot as plt

# File path to the uploaded NetCDF file
file_path = '../data/Vegetation_ET/FLDAS_NOAH01_C_GL_M.A202408.001.nc'

# Open the NetCDF file using xarray
ds = xr.open_dataset(file_path)

# Print the dataset to explore its structure and variables
print(ds)

import matplotlib.pyplot as plt

# Evap_tavg 변수 추출
evap_data = ds['Evap_tavg']

# 특정 시간에 대한 데이터 선택 (예: 첫 번째 time step)
time_index = 0  # 첫 번째 시간
evap_at_time = evap_data.isel(time=time_index)

# Evapotranspiration 데이터 시각화
plt.figure(figsize=(10, 6))
evap_at_time.plot(cmap='viridis')  # colormap은 취향에 따라 변경 가능
plt.title(f'Evapotranspiration at time index {time_index}')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()