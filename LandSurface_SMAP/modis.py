import json

import cv2
import requests
from pydap.client import open_url
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

import numpy as np

class ModisL4Dataset:



    def __init__(self):
        self.field_list = ['LST_Day_1km', 'LST_Night_1km']
        self.desc = "MODIS/Terra Land Surface Temperature/Emissivity Daily L3 Global 1km SIN Grid V061"
        self.data_shape = (2400, 2400)
        self.dict_ds = {}
        edl_token = 'eyJ0eXAiOiJKV1QiLCJvcmlnaW4iOiJFYXJ0aGRhdGEgTG9naW4iLCJzaWciOiJlZGxqd3RwdWJrZXlfb3BzIiwiYWxnIjoiUlMyNTYifQ.eyJ0eXBlIjoiVXNlciIsInVpZCI6Imx6YWsiLCJleHAiOjE3MzI3ODI5NTcsImlhdCI6MTcyNzU5ODk1NywiaXNzIjoiaHR0cHM6Ly91cnMuZWFydGhkYXRhLm5hc2EuZ292In0.CllLCWRe-eTXYG9S6grq63e62eGeOMR4YKcyRkvPJAn4uvfSr8mttJYiQHB9ByPbmIqFyp_xf5iOTlCVsJ4TyIPHvK63s40jE9WJPpwja_DgZZdUbLrRHDkMntLq_I4qaHKvvciqn6i6RnTQ8r5S4d1qROKLWyS0b-ELG07rv-3b5BZ9F5dIiLZFLhp06su6B6JFQpMx9GJ976kaTiPa-B918MtcoykiSrmp_YTE0o_JwjC8JWkUzcTOJmf6heegONqDtF5tTzmWo2cxMq5rFn33m9IyGjjxNvrFHqVoZwpfSm6-v5j4GH6k8rUul_NmvH_cxAkPpEQJ9xbmIz1_WQ'

        auth_hdr = "Bearer " + edl_token
        my_session = requests.Session()
        my_session.headers = {"Authorization": auth_hdr}
        import numpy as np
        # OPeNDAP URL
        dataset_url_1 = 'https://opendap.cr.usgs.gov/opendap/hyrax/DP128/MOLT/MOD11A1.061/2024.10.02/MOD11A1.A2024276.h20v06.061.2024277100817.hdf'
        dataset_url_2 = 'https://opendap.cr.usgs.gov/opendap/hyrax/DP128/MOLT/MOD11A1.061/2024.10.02/MOD11A1.A2024276.h20v05.061.2024277100827.hdf'
        dataset_url_3 = 'https://opendap.cr.usgs.gov/opendap/hyrax/DP128/MOLT/MOD11A1.061/2024.10.02/MOD11A1.A2024276.h21v06.061.2024277101035.hdf'
        dataset_url_4 = 'https://opendap.cr.usgs.gov/opendap/hyrax/DP128/MOLT/MOD11A1.061/2024.10.02/MOD11A1.A2024276.h21v05.061.2024277100832.hdf'

        dataset_1 = open_url(dataset_url_1, session=my_session, protocol='dap4')
        dataset_2 = open_url(dataset_url_2, session=my_session, protocol='dap4')
        dataset_3 = open_url(dataset_url_3, session=my_session, protocol='dap4')
        dataset_4 = open_url(dataset_url_4, session=my_session, protocol='dap4')

        # np array로 바꿀수 있는것만 변환




        for key in self.field_list:
            # dataset 1~4 를 합처서 2400 * 2400 모양의 np array로 만들어야함
            foo = dataset_3[key]
            top_row = np.hstack([np.array(dataset_2[key]), np.array(dataset_4[key])])
            bottom_row = np.hstack([np.array(dataset_1[key]), np.array(dataset_3[key])])
            self.dict_ds[key] =np.vstack([top_row, bottom_row])


            print(key + " loaded")

        print(self.dict_ds.keys())





if __name__ == '__main__':
    modis = ModisL4Dataset()




