import netCDF4 as nc

# OPeNDAP URL (기후 강수량 데이터를 제공하는 예시)
url = 'https://gpm1.gesdisc.eosdis.nasa.gov/opendap/hyrax/GPM_L3/GPM_3IMERGHHE.07/2024/274/3B-HHR-E.MS.MRG.3IMERG.20240930-S223000-E225959.1350.V07B.HDF5'

# 파일 열기
dataset = nc.Dataset(url)

# 변수 목록 확인
print(dataset.variables.keys())

# 특정 변수(예: 강수량) 데이터 접근
precipitation = dataset.variables['precipitation'][:]
print(precipitation)
