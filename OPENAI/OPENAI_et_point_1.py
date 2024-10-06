import xarray as xr
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# File path to the uploaded NetCDF file
file_path = '../data/Vegetation_ET/FLDAS_NOAH01_C_GL_M.A202408.001.nc'

# Open the NetCDF file using xarray
ds = xr.open_dataset(file_path)

# Evap_tavg 변수 추출
evap_data = ds['Evap_tavg']


# 특정 위도(Y)와 경도(X) 좌표 선택 (예시: 경도 120, 위도 -30)
lon = 120  # 경도
lat = -30  # 위도

# 가장 가까운 좌표에 해당하는 값을 추출
evap_value = evap_data.sel(X=lon, Y=lat, method='nearest').values

# 출력
print(f'경도 {lon}, 위도 {lat}에서의 증발산 값: {evap_value}')

