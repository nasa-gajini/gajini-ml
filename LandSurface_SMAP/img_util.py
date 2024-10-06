import json
import numpy as np
import cv2
import requests
from pydap.client import open_url
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


def np_array_to_rgba_image(np_array, vmin, vmax):
    normalized_array = (np.clip(np_array, vmin, vmax) - vmin) / (vmax-vmin)  # Ensure values are within 0-1500

    colormap = plt.cm.plasma
    rgba_array = colormap(normalized_array)
    rgba_array[..., 3] = (normalized_array > 0).astype(np.float32)  # Make 0 values transparent
    rgba_array = (rgba_array * 255).astype(np.uint8)
    return rgba_array


def np_array_to_gray_image(np_array, vmin, vmax):
    normalized_array = (np.clip(np_array, vmin, vmax) - vmin) / (vmax-vmin)  # Ensure values are within 0-1500

    # uint8 gray img (0~255)  변환
    gray_array = (normalized_array * 255).astype(np.uint8)


    return gray_array


def merge_img(img1, img2):
    sum_img = img1.copy()
    # 결측치 비율을 계산하는 함수

    if img1.dtype == np.float32:
        sum_img[sum_img == -9999.0] = img2[sum_img == -9999.0]

    elif img1.dtype == np.uint16:
        sum_img[sum_img == 65534] = img2[sum_img == 65534]

    elif img1.dtype == np.uint8:
        sum_img[sum_img == 254] = img2[sum_img == 254]

    return sum_img
