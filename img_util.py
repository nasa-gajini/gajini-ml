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

    return rgba_array