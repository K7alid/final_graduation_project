
from gradio_client import Client, file
from datetime import datetime
import cloudinary

import cloudinary.uploader


from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

def download_image(url, path):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(path, 'wb') as f:
                f.write(response.content)
            return path
        else:
            return None
    except requests.RequestException as e:
        print(f"Error downloading image: {e}")
        return None



def model_predict(user_picture_path, garment_image_path):
    client = Client("yisol/IDM-VTON")

    result = client.predict(
        dict={
            "background": file(user_picture_path),
            "layers": [],  # Make sure this is an empty list if no layers are used
            "composite": None  # Use None if no composite image is used
        },
        garm_img=file(garment_image_path),
        garment_des="Hello!!",  # Example garment description
        is_checked=True,  # Checkbox is checked
        is_checked_crop=False,  # Checkbox for crop is not checked
        denoise_steps=30,  # Number of denoise steps
        seed=42,  # Random seed for process consistency
        api_name="/tryon"  # API endpoint
    )

    return result

# def upload_to_imgur(image_path, client_id):
#     headers = {'Authorization': 'Client-ID ' + client_id}
#     url = 'https://api.imgur.com/3/image'
#     try:
#         with open(image_path, 'rb') as image:
#             data = {'image': image.read()}
#             response = requests.post(url, headers=headers, files=data)
#             if response.status_code == 200:
#                 response_data = response.json()
#                 if response_data['success']:
#                     return response_data['data']['link']
#             return None
#     finally:
#         os.remove(image_path)  # Clean up the image file




def upload_image(image_path):

    cloudinary.config(
        cloud_name="ddy3f2qew",
        api_key="763657237474537",
        api_secret="bLQ0lTAq1b1TQdTjKhjW3su64wA"
    )


    id = datetime.now().isoformat().replace(':', '').replace('.','').replace('-','')
    cloudinary.uploader.upload(image_path,
                               public_id=id)

    from cloudinary.utils import cloudinary_url

    url, options = cloudinary_url(id, format='jpg')

    print(url)
    return url





@app.route('/')
def home():
    return "Hello, World!"

@app.route('/process_images', methods=['POST'])
def process_images():
    data = request.get_json()
    user_picture_url = data['user_picture_url']
    garment_image_url = data['garment_image_url']

    user_picture_path = download_image(user_picture_url, 'user_picture.jpg')
    garment_image_path = download_image(garment_image_url, 'garment_picture.jpg')

    if not user_picture_path or not garment_image_path:
        return jsonify({'error': 'Failed to download images'}), 400

    model_prediction = model_predict(user_picture_path, garment_image_path)
    if not model_prediction:
        return jsonify({'error': 'Failed to process images'}), 500
    # imgur_client_id = '582fe74c9292bda'

    uploaded_image_url = upload_image(model_prediction[0])
    if not uploaded_image_url:
        return jsonify({'error': 'Failed to upload image to Imgur'}), 500

    return jsonify({'new_image_url': uploaded_image_url})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    process_images()

# ngrok
#ngrok config add-authtoken 2fkEPj0AZkMbZ9fgakiE858QZ9d_5cNRFSbT5VYRFsbT9x5Ms
#ngrok http 5000