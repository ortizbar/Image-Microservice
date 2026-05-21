# Image-Microservice

## Description
The Image Microservice generates image responses based on requests from other programs.

## Communication Pipe
REST API using HTTP POST requests and JSON responses.

## How to Request Data

## Endpoint:

```
http://localhost:5003/generate-image
```

## Example Request:

```
json = {
  "request_type": "meal_image",
  "prompt": "healthy chicken salad",
  "image_format": "png",
  "data": "meal information"
}
```

## Example Python Request:

```
import requests
response = requests.post(
  "http://localhost:5003/generate-image",
  json = {
    "request_type": "meal_image",
    "prompt": "healthy chicken salad",
    "image_format": "png",
    "data": "meal information"
  }
)
print(response.json())
```

## How to Receive Data

Example Response:

```
Test program sent request to Image Microservice.
Test program received response from Image Microservice:
{'image_url': 'https://www.naturemade.com/cdn/shop/articles/healthy-foods-to-eat_960x.jpg?v=1611988563', 'message': 'Image generated successfully', 'status': 'success'}
```

UML Sequence Diagram

<img width="1063" height="587" alt="Screenshot 2026-05-20 200907" src="https://github.com/user-attachments/assets/9c98d141-1f38-4c59-99a1-c9a164d36f85" />
