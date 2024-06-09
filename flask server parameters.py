# this server code is not using the replicate api but using the gradio api and with parameters
# this server code is not using the replicate api but using the gradio api and with parameters
# this server code is not using the replicate api but using the gradio api and with parameters
# this server code is not using the replicate api but using the gradio api and with parameters

#it's working alhamdullah


# def download_image(url, path):
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             with open(path, 'wb') as f:
#                 f.write(response.content)
#             return path
#         else:
#             return None
#     except requests.RequestException as e:
#         print(f"Error downloading image: {e}")
#         return None
#


import requests
from PIL import Image
def download_image(url, path, size=(768, 1024)):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(path, 'wb') as f:
                f.write(response.content)

            with Image.open(path) as img:
                resized_img = img.resize(size)
                resized_img.save(path)

            return path
        else:
            return None
    except requests.RequestException as e:
        print(f"Error downloading image: {e}")
        return None


from gradio_client import Client, file
def model_generation(human_img, garm_img):
    client = Client("yisol/IDM-VTON")

    result = client.predict(
        dict={
            "background": file(human_img),
            "layers": [],
            "composite": None
        },
        garm_img=file(garm_img),
        garment_des="Hello!!",
        is_checked=True,
        is_checked_crop=False,
        denoise_steps=30,
        seed=42,
        api_name="/tryon"
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



from datetime import datetime
def makeUID():
    return (datetime.now().isoformat().replace(':', '')
          .replace('.','').replace('-',''))



import cloudinary
import cloudinary.uploader
def upload_generated_image(image_path):

    cloudinary.config(
        cloud_name="ddy3f2qew",
        api_key="763657237474537",
        api_secret="bLQ0lTAq1b1TQdTjKhjW3su64wA"
    )

    id = makeUID()
    cloudinary.uploader.upload(image_path,
                               public_id=id)
    from cloudinary.utils import cloudinary_url
    url, options = cloudinary_url(id, format='jpg')
    print(url)
    url = url.replace("http://", "https://")
    print(url)
    return url


import shutil
def move_file(src, dst):
    shutil.move(src, dst)


from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/', methods=['GET', "POST"])
def process_image():
    human_img = request.args.get('human_img')
    garm_img = request.args.get('garm_img')

    if not human_img or not garm_img:
        return jsonify({'error': 'Missing image URLs'}), 400

    id = makeUID()
    human_img = download_image(human_img, f'pictures/{id}_human_img.jpg')
    garm_img = download_image(garm_img, f'pictures/{id}_garm_img.jpg')
    # human_img = download_image(human_img, 'human_img.jpg')
    # garm_img = download_image(garm_img, 'garm_img.jpg')

    if not human_img or not garm_img:
        return jsonify({'error': 'Failed to download images'}), 400

    model_prediction = model_generation(human_img, garm_img)
    if not model_prediction:
        return jsonify({'error': 'Failed to process images'}), 500

    print(model_prediction)
    print(model_prediction[0])
    uploaded_image_url = upload_generated_image(model_prediction[0])
    print(uploaded_image_url)
    move_file(model_prediction[0], f'pictures/{id}_new_image.jpg')
    if not uploaded_image_url:
        return jsonify({'error': 'Failed to upload image to Imgur'}), 500
    return jsonify({'new_image_url': uploaded_image_url})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    process_image()

# ngrok
#ngrok config add-authtoken 2fkEPj0AZkMbZ9fgakiE858QZ9d_5cNRFSbT5VYRFsbT9x5Ms
#ngrok http 5000