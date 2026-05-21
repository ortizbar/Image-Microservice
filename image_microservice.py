from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/generate-image', methods=['POST'])
def generate_image():
    data = request.json

    request_type = data.get("request_type")
    prompt = data.get("prompt")
    image_format = data.get("image_format")
    extra_data = data.get("data")

    if not request_type or not prompt or not image_format or not extra_data:
        return jsonify({
            "status": "error",
            "message": "Invalid request data"
        })

    if image_format not in ["png", "jpeg", "jpg"]:
        return jsonify({
            "status": "error",
            "message": "Unsupported image format"
        })

    return jsonify({
        "status": "success",
        "image_url": "https://www.naturemade.com/cdn/shop/articles/healthy-foods-to-eat_960x.jpg?v=1611988563",
        "message": "Image generated successfully"
    })

if __name__ == "__main__":
    app.run(port=5003)
