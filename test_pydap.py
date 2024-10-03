import requests
from pydap.client import open_url
import h5py
from pydap.cas.urs import setup_session
edl_token = 'eyJ0eXAiOiJKV1QiLCJvcmlnaW4iOiJFYXJ0aGRhdGEgTG9naW4iLCJzaWciOiJlZGxqd3RwdWJrZXlfb3BzIiwiYWxnIjoiUlMyNTYifQ.eyJ0eXBlIjoiVXNlciIsInVpZCI6Imx6YWsiLCJleHAiOjE3MzI3ODI5NTcsImlhdCI6MTcyNzU5ODk1NywiaXNzIjoiaHR0cHM6Ly91cnMuZWFydGhkYXRhLm5hc2EuZ292In0.CllLCWRe-eTXYG9S6grq63e62eGeOMR4YKcyRkvPJAn4uvfSr8mttJYiQHB9ByPbmIqFyp_xf5iOTlCVsJ4TyIPHvK63s40jE9WJPpwja_DgZZdUbLrRHDkMntLq_I4qaHKvvciqn6i6RnTQ8r5S4d1qROKLWyS0b-ELG07rv-3b5BZ9F5dIiLZFLhp06su6B6JFQpMx9GJ976kaTiPa-B918MtcoykiSrmp_YTE0o_JwjC8JWkUzcTOJmf6heegONqDtF5tTzmWo2cxMq5rFn33m9IyGjjxNvrFHqVoZwpfSm6-v5j4GH6k8rUul_NmvH_cxAkPpEQJ9xbmIz1_WQ'

auth_hdr="Bearer " + edl_token
my_session = requests.Session()
my_session.headers={"Authorization": auth_hdr}
import numpy as np
# OPeNDAP URL
dataset_url = 'https://gpm1.gesdisc.eosdis.nasa.gov/opendap/hyrax/GPM_L3/GPM_3IMERGHHE.07/2024/274/3B-HHR-E.MS.MRG.3IMERG.20240930-S223000-E225959.1350.V07B.HDF5'
file_path = './SMAP_L3_SM_P_E_20240801_R19240_002.h5'
gpm_ds = open_url(dataset_url, session=my_session, protocol='dap4')


smap_ds = h5py.File(file_path, 'r')


def print_name(name):
    print(name)

smap_ds.visit(print_name)

gpm_ds.tree()
# 데이터셋에서 변수 접근

# 위도와 경도 데이터 로드
# 위도와 경도 데이터 로드 및 배열 변환
latitudes = np.array(gpm_ds['lat'][:])
longitudes = np.array(gpm_ds['lon'][:])
# 주어진 좌표
target_lat = 40.56163122754966,
target_lon = -81.03959074276007

# 가장 가까운 위도와 경도 인덱스 찾기
lat_idx = int(np.abs(latitudes - target_lat).argmin())
lon_idx = int(np.abs(longitudes - target_lon).argmin())

# 강수량과 강수 확률 데이터 로드
shape = gpm_ds['precipitation'].shape
print(shape)



precipitation = gpm_ds['precipitation']#[:,lat_idx,lon_idx]
probabilityLiquidPrecipitation = gpm_ds['probabilityLiquidPrecipitation']
precipitation_np = np.array(gpm_ds['probabilityLiquidPrecipitation'])
soil_moisture = smap_ds['Soil_Moisture_Retrieval_Data_AM/soil_moisture']
soil_moisture_np = np.array(soil_moisture)
print(soil_moisture_np)