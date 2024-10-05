import requests
from pydap.client import open_url


class GpmL3Dataset:
    def __init__(self):
        edl_token = 'eyJ0eXAiOiJKV1QiLCJvcmlnaW4iOiJFYXJ0aGRhdGEgTG9naW4iLCJzaWciOiJlZGxqd3RwdWJrZXlfb3BzIiwiYWxnIjoiUlMyNTYifQ.eyJ0eXBlIjoiVXNlciIsInVpZCI6Imx6YWsiLCJleHAiOjE3MzI3ODI5NTcsImlhdCI6MTcyNzU5ODk1NywiaXNzIjoiaHR0cHM6Ly91cnMuZWFydGhkYXRhLm5hc2EuZ292In0.CllLCWRe-eTXYG9S6grq63e62eGeOMR4YKcyRkvPJAn4uvfSr8mttJYiQHB9ByPbmIqFyp_xf5iOTlCVsJ4TyIPHvK63s40jE9WJPpwja_DgZZdUbLrRHDkMntLq_I4qaHKvvciqn6i6RnTQ8r5S4d1qROKLWyS0b-ELG07rv-3b5BZ9F5dIiLZFLhp06su6B6JFQpMx9GJ976kaTiPa-B918MtcoykiSrmp_YTE0o_JwjC8JWkUzcTOJmf6heegONqDtF5tTzmWo2cxMq5rFn33m9IyGjjxNvrFHqVoZwpfSm6-v5j4GH6k8rUul_NmvH_cxAkPpEQJ9xbmIz1_WQ'

        auth_hdr = "Bearer " + edl_token
        my_session = requests.Session()
        my_session.headers = {"Authorization": auth_hdr}
        import numpy as np
        # OPeNDAP URL
        dataset_url = 'https://gpm1.gesdisc.eosdis.nasa.gov/opendap/hyrax/GPM_L3/GPM_3IMERGHHE.07/2024/274/3B-HHR-E.MS.MRG.3IMERG.20240930-S223000-E225959.1350.V07B.HDF5'
        self.gpm_ds = open_url(dataset_url, session=my_session, protocol='dap4')
        # np array로 바꿀수 있는것만 변환

        self.dict_ds={}


        for key in self.gpm_ds.keys():

            self.dict_ds[key] = np.array(self.gpm_ds[key][:])
            print(key + " loaded")



gpm3 = GpmL3Dataset()



