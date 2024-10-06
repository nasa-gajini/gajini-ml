

#--------------------------------------------------------
# SMAP 데이터 변수 값 샘플
# Soil moisture (토양 수분 함량): 0.2 (단위: m³/m³, 0에서 1 사이의 값, 0은 매우 건조, 1은 매우 습함)
# Vegetation water content (식물 수분 함량): 0.15 (단위: kg/m², 식물 내 수분의 양)
# Vegetation opacity (식물 불투명도): 0.8 (식물의 광학적 두께, 0은 완전히 투명, 1은 불투명)
# Bulk density (토양의 부피 밀도): 1.3 (단위: g/cm³, 일반적으로 1.1~1.7 g/cm³ 범위)
# Clay fraction (토양 내 점토 함량): 0.25 (0에서 1 사이의 값, 1은 100% 점토)
# Surface temperature (지표면 온도): 300 (단위: K, 켈빈, 대략 섭씨 27도)
# Static Water Body Fraction (정적 수체 비율): 0.1 (수역의 비율, 0에서 1 사이)
# NDVI (Normalized Difference Vegetation Index) 값 샘플
#--------------------------------------------------------
# SMAP
soil_moisture = 0.2
vegetation_water_content = 0.15
vegetation_opacity = 0.8
bulk_density = 1.3
clay_fraction = 0.25
surface_temperature = 300  # K (Kelvin)
static_water_body_fraction = 0.1

#--------------------------------------------------------
# NDVI
# NDVI: 0.65 (0에서 1 사이의 값, 1은 완전히 녹색 식물로 덮인 상태, 0은 식생이 거의 없음)
#--------------------------------------------------------
ndvi = 0.65

#--------------------------------------------------------
# ET_POINT
# ET_POINT (Evapotranspiration, 증발산량) 값 샘플
#--------------------------------------------------------
et = 4.5

import os
import requests
import xarray as xr
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get OpenAI API key from .env
openai_api_key = os.getenv("OPENAI_API_KEY")


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

