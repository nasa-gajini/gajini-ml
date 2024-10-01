import h5py
import numpy as np
# HDF5 파일 경로
file_path = './tmp/SMAP_L3_SM_P_E_20240929_R19240_002.h5'

# 파일 열기

# 파일 열기
with h5py.File(file_path, 'r') as file:
    # 파일 내의 데이터셋과 그룹 구조를 출력 (탐색용)
    def print_name(name):
        print(name)
    file.visit(print_name)

    # 위도와 경도 데이터셋 로드
    if 'Soil_Moisture_Retrieval_Data_AM/latitude' in file and 'Soil_Moisture_Retrieval_Data_AM/longitude' in file:
        latitudes = file['Soil_Moisture_Retrieval_Data_AM/latitude'][:]
        longitudes = file['Soil_Moisture_Retrieval_Data_AM/longitude'][:]

        # 주어진 위도와 경도
        target_lat = 40.0
        target_lon = -81.0

        # 각 지점의 위도와 경도와의 차이 계산
        lat_lon_diff = np.sqrt((latitudes - target_lat)**2 + (longitudes - target_lon)**2)

        # 가장 작은 차이를 가진 지점의 인덱스 찾기
        lat_idx, lon_idx = np.unravel_index(lat_lon_diff.argmin(), lat_lon_diff.shape)

        # 토양 수분 데이터셋 접근
        if 'Soil_Moisture_Retrieval_Data_AM/soil_moisture' in file:
            soil_moisture = file['Soil_Moisture_Retrieval_Data_AM/soil_moisture'][lat_idx, lon_idx]
            print(f"Soil Moisture Data at Latitude {target_lat} and Longitude {target_lon}:")
            print("Soil moisture : "+str(soil_moisture) + "%")
        else:
            print("Soil moisture dataset not found in the file.")
    else:
        print("Latitude or longitude dataset not found in the file.")