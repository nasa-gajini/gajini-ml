import h5py
import numpy as np
# HDF5 파일 경로
file_path = './SMAP_L3_SM_P_E_20240801_R19240_002.h5'

# 파일 열기

# 파일 열기
with h5py.File(file_path, 'r') as file:
    # 파일 내의 데이터셋과 그룹 구조를 출력 (탐색용)
    def print_name(name):
        print(name)
    file.visit(print_name)