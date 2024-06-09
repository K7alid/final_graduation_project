# this is the code for the replicate api with flask server and using api with body
# this is the code for the replicate api with flask server and using api with body
# this is the code for the replicate api with flask server and using api with body
# this is the code for the replicate api with flask server and using api with body
# this is the code for the replicate api with flask server and using api with body


from flask import Flask, request, jsonify
import replicate
import os

app = Flask(__name__)

# Set up the Replicate API
os.environ["REPLICATE_API_TOKEN"] = "r8_5fAKRjEI8fBGOQEPeswasgDtsPZ7GM21L5Uic"
#r8_SmCU44jUTz90Q21QuXlq9NWDuUtuqgk1IE3qY
#r8_8G73rzoXozjxS7of7yUTaXngl3bkdOf3NmgVs
api = replicate.Client(api_token=os.environ["REPLICATE_API_TOKEN"])

@app.route('/', methods=['GET', "POST"])
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
