import requests

response = requests.post(
    "http://localhost:5003/generate-image",
    json={
        "request_type": "meal_image",
        "prompt": "healthy salad",
        "image_format": "png",
        "data": "meal information"
    }
)

print("Test program sent request to Image Microservice.")
print("Test program received response from Image Microservice:")
print(response.json())
