import os
import base64
import requests
from dotenv import load_dotenv
from PIL import Image

# Load environment variables from .env file
load_dotenv()

# Get OpenAI API key from .env
openai_api_key = os.getenv("OPENAI_API_KEY")


# Function to read and display image
def read_image(image_path):
    image = Image.open(image_path)
    image.show()  # This will display the image
    return image


# Function to encode the image in base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


# Function to get image description from OpenAI API
def image_describe_by_prompt(prompt, image_path):
    base64_image = encode_image(image_path)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}"
    }

    payload = {
        "model": "gpt-4o",
        "messages": [
            {
                "role": "user",
                "content": f"{prompt}"
            },
            {
                "role": "user",
                "content": f"data:image/jpeg;base64,{base64_image}"
            }
        ],
        "max_tokens": 300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    # Handle response and check for errors
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code}, {response.text}"


# Main function
def main():
    image_path = "../data/img/egypt_evap_combined_emphasized.png"
    prompt = "이 이미지는 나사의 2024년과 2023년의 egpyt 통계값으로 evap지수 (즉, Evapotranspiration (ET) is the sum of evaporation from the land surface and transpiration in vegetation.값인 ET의 평균값으로,지면에서 증발되고 식물에서 증발하는 물의 양을 나타내는 변수로, 물 순환과 에너지 흐름에서 중요한 역할을 합니다. 이 데이터셋에서의 증발산량은 주어진 시간 동안 평균된 값입니다. 해당 이미지를 바탕으로 이집트의 농업에 대해 요약하고 설명해주세요. 한국어로 설명해야 합니다. "

    # Display the image
    read_image(image_path)

    # Get image description from OpenAI API
    image_description = image_describe_by_prompt(prompt, image_path)

    # Print the image description
    print("Image Description:", image_description)


if __name__ == "__main__":
    main()
