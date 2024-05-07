from flask import Flask, request, jsonify
import replicate
import os

app = Flask(__name__)

# Set up the Replicate API
api = replicate.Client(api_token='r8_AuwRCDwCsFbXpGpyZtSbrYzauQ2Mkwh1xqWTY')

@app.route('/transform', methods=['POST'])
def transform():
    data = request.json
    garm_img = data.get('garm_img')
    human_img = data.get('human_img')

    if not all([garm_img, human_img]):
        return jsonify({"error": "Missing data, ensure all fields are provided."}), 400

    try:
        input = {
            "garm_img": garm_img,
            "human_img": human_img,
            "garment_des": 'cute pink top'
        }
        output = api.run(
            "cuuupid/idm-vton:906425dbca90663ff5427624839572cc56ea7d380343d13e2a4c4b09d3f0c30f",
            input=input
        )
        return jsonify({"new_image_url": output})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)



# # A very simple Flask Hello World app for you to get started with...
#
# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route('/')
# def hello_world():
#     return 'Hello from Flask!'
#
