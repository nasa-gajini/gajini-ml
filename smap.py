import h5py
import numpy as np



class SmapDataset:
    def __init__(self, file_path):

        # 파일 열기
        file = h5py.File(file_path, 'r')

        self.ds_dict = {}

        print(file.keys())
        for key in file.keys():
            # np array로 바꿀수 있는것만 변환
            # 하위 데이터 딕셔너리도 모두 순회하며 np array로 변환
            if isinstance(file[key], h5py.Dataset):
                self.ds_dict[key] = np.array(file[key])
            else:
                self.ds_dict[key] = {}
                for sub_key in file[key].keys():
                    self.ds_dict[key][sub_key] = np.array(file[key][sub_key])






if __name__ == '__main__':
    # HDF5 파일 경로
    file_path = './data/SMAP_L3_SM_P_E_20240801_R19240_002.h5'
    smap = SmapDataset(file_path)
    moi = smap.ds_dict['Soil_Moisture_Retrieval_Data']['soil_moisture']
    print(moi.shape)

