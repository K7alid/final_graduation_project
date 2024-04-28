import aiohttp
import asyncio
import argparse


async def upload_images(api_url, user_image_url, garment_image_url):
    data = {
        "user_picture_url": user_image_url,
        "garment_image_url": garment_image_url
    }
    headers = {'Content-Type': 'application/json'}

    async with aiohttp.ClientSession() as session:
        async with session.post(api_url, json=data, headers=headers) as response:
            if response.status == 200:
                return await response.json()
            else:
                return f"Failed to get a valid response from the server, status code: {response.status}"


async def main(api_url, user_image_url, garment_image_url):
    result = await upload_images(api_url, user_image_url, garment_image_url)

    if isinstance(result, dict):
        print(f"Image successfully processed, URL: {result.get('new_image_url')}")
    else:
        print(result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upload images for processing")
    parser.add_argument(
        'api_url',
        type=str,
        # default='http://127.0.0.1:5000/process_images',
        default='http://192.168.5.4:5000/process_images',
        nargs='?',
        help="API URL to submit images"
    )
    parser.add_argument(
        'user_image_url',
        type=str,
        default='https://yisol-idm-vton.hf.space/file=/tmp/gradio/c74e02439c793759822def314c4475876fe457b3/sam1%201.jpg',
        nargs='?',
        help="URL of the user image (default URL provided)"
    )
    parser.add_argument(
        'garment_image_url',
        type=str,
        default='https://yisol-idm-vton.hf.space/file=/tmp/gradio/a3c941bfdd20a074b05550e93715dd720ac9442b/09163_00.jpg',
        nargs='?',
        help="URL of the garment image (default URL provided)"
    )
    args = parser.parse_args()

    asyncio.run(main(args.api_url, args.user_image_url, args.garment_image_url))
# Compare this snippet from main.py: