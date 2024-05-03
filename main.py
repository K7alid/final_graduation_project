# import requests
# from gradio_client import Client, file
#
# def download_image(url, path):
#     response = requests.get(url)
#     if response.status_code == 200:
#         with open(path, 'wb') as f:
#             f.write(response.content)
#     else:
#         raise Exception(f"Failed to download image from {url}")
#
# # Download images
# user_picture = 'background.jpg'
# garment_image_path = 'garment.jpg'
# download_image('https://yisol-idm-vton.hf.space/file=/tmp/gradio/c74e02439c793759822def314c4475876fe457b3/sam1%201.jpg', user_picture)
# download_image('https://yisol-idm-vton.hf.space/file=/tmp/gradio/5b514fb0d69c0c58f571777d2b3c55649ccc44df/09176_00.jpg', garment_image_path)
#
# client = Client("yisol/IDM-VTON")
#
# result = client.predict(
#     dict={
#         "background": file(user_picture),
#         "layers": [],  # Make sure this is an empty list if no layers are used
#         "composite": None  # Use None if no composite image is used
#     },
#     garm_img=file(garment_image_path),
#     garment_des="Hello!!",  # Example garment description
#     is_checked=True,       # Checkbox is checked
#     is_checked_crop=False, # Checkbox for crop is not checked
#     denoise_steps=30,      # Number of denoise steps
#     seed=42,               # Random seed for process consistency
#     api_name="/tryon"      # API endpoint
# )
#
# print(result)
# print(result[0])
# print(result[1])
#
# import requests
#
#
# def upload_to_imgur(image_path, client_id):
#     headers = {'Authorization': f'Client-ID {client_id}'}
#     url = 'https://api.imgur.com/3/image'
#
#     with open(image_path, 'rb') as image:
#         data = {'image': image.read()}
#         response = requests.post(url, headers=headers, files=data)
#         response_data = response.json()
#
#         if response.status_code == 200 and response_data['success']:
#             return response_data['data']['link']
#         else:
#             raise Exception(f"Failed to upload image: {response_data['data']['error']}")
#
#
# client_id = '582fe74c9292bda'  # Replace with your actual Imgur client ID
# image_path = result[0] # 'output_image.jpg
# try:
#     img_url = upload_to_imgur(image_path, client_id)
#     print(f"Image successfully uploaded: {img_url}")
# except Exception as e:
#     print(str(e))
#



# Import necessary library
from gradio_client import Client, file

# Set up the Gradio client
client = Client("yisol/IDM-VTON")

# Define the parameters for the API call
inputs = {
    "dict": {
        "background": file('model_1.png'),  # Replace with your background image path
        "layers": [],  # Add any additional layers if applicable
        "composite": None  # Use None or provide a path if needed
    },
    "garm_img": file('Shirts/5.png'),  # Replace with your garment image path
    "garment_des": "A brief description of your garment",
    "is_checked": True,  # True or False depending on your requirement
    "is_checked_crop": False,  # True or False depending on your requirement
    "denoise_steps": 30,  # Can adjust the number of denoising steps if needed
    "seed": 42  # Adjust the seed for random processes if needed
}

# Perform the API call to try on the garment
result = client.predict(**inputs, api_name="/tryon")

# Print the results
print(result)
