# import xarray as xr
# import matplotlib.pyplot as plt
# import matplotlib.pyplot as plt
#
# # File path to the uploaded NetCDF file
# file_path = './data/Vegetation_ET/FLDAS_NOAH01_C_GL_M.A202408.001.nc'
#
# # Open the NetCDF file using xarray
# ds = xr.open_dataset(file_path)
#
# # Evap_tavg 변수 추출
# evap_data = ds['Evap_tavg']
#
# print(evap_data)
# print(evap_data['X'])
#
# # 특정 위도(Y)와 경도(X) 좌표 선택 (예시: 경도 120, 위도 -30)
# lon = 120  # 경도
# lat = -30  # 위도
#
# # 가장 가까운 좌표에 해당하는 값을 추출
# evap_value = evap_data.sel(X=lon, Y=lat, method='nearest').values
#
# # 출력
# print(f'경도 {lon}, 위도 {lat}에서의 증발산 값: {evap_value}')


import os
import base64
import requests
import xarray as xr
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get OpenAI API key from .env
openai_api_key = os.getenv("OPENAI_API_KEY")


# Function to encode the image in base64 (for future use if you want to send images)
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


# Function to extract Evap_tavg value based on lon and lat
def extract_evap_data(file_path, lon, lat):
    # Open the NetCDF file using xarray
    ds = xr.open_dataset(file_path)

    # Evap_tavg 변수 추출
    evap_data = ds['Evap_tavg']

    # 가장 가까운 좌표에 해당하는 값을 추출
    evap_value = evap_data.sel(X=lon, Y=lat, method='nearest').values

    return evap_value


# Function to query OpenAI API for the extracted data
def query_openai(prompt, evap_value, lon, lat):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}"
    }

    # Create a question for the AI including the extracted Evap_tavg value
    user_question = f"{prompt} 위도 {lat}, 경도 {lon}에서의 증발산 값은 {evap_value}입니다. 이 수치를 바탕으로 이집트 농업에 대한 영향을 분석해주세요."

    payload = {
        "model": "gpt-4",
        "messages": [
            {
                "role": "user",
                "content": user_question
            }
        ],
        "max_tokens": 500
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    # Handle response and check for errors
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code}, {response.text}"


# Main function
def main():
    # Define file path and the coordinates (lon, lat) you want to query
    file_path = '../data/Vegetation_ET/FLDAS_NOAH01_C_GL_M.A202408.001.nc'
    lon = 31.233  # 카이로의 경도
    lat = 30.033  # 카이로의 위도

    # Extract Evap_tavg data for the given coordinates
    evap_value = extract_evap_data(file_path, lon, lat)

    # Define a prompt to ask OpenAI
    prompt = "이 값은 Evapotranspiration (ET) 수치로, 해당 값은 물 순환과 에너지 흐름에서 중요한 역할을 합니다. "

    # Get description from OpenAI based on the extracted value
    response = query_openai(prompt, evap_value, lon, lat)

    # Print the response from OpenAI
    print("AI Response:", response)


if __name__ == "__main__":
    main()

