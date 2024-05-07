# this is the code for the replicate api with flask server and using api with parameters not body
# this is the code for the replicate api with flask server and using api with parameters not body
# this is the code for the replicate api with flask server and using api with parameters not body
# this is the code for the replicate api with flask server and using api with parameters not body

#it's working alhamdullah

import replicate

from flask import Flask, request, jsonify
import json
import time

app = Flask(__name__)

@app.route('/', methods=['GET', "POST"])
def handle_request():

    human_img = str(request.args.get('human_img'))
    garm_img = str(request.args.get('garm_img'))
    api = replicate.Client(api_token='r8_6UqgQALK1tyDpiRNhqOPgvEZPpKgmJS31Tf0R')#r8_SmCU44jUTz90Q21QuXlq9NWDuUtuqgk1IE3qY

    input = {
        "garm_img": garm_img,
        "human_img": human_img,
        "garment_des": "cute pink top"
    }

    output = api.run(
        "cuuupid/idm-vton:906425dbca90663ff5427624839572cc56ea7d380343d13e2a4c4b09d3f0c30f",
        input=input
    )
    data_set = {"new_image_url": output}
    json_dump = json.dumps(data_set)
    return json_dump

if __name__ == '__main__':
    app.run(debug=True)


# import replicate
#
#
# import os
# import replicate
#
# #Set the REPLICATE_API_TOKEN environment variable
# os.environ["REPLICATE_API_TOKEN"] = "r8_buLTfoRw7E7A32AIPDteMYnrmZZPVrk3KgkJb"
# api = replicate.Client(api_token=os.environ["REPLICATE_API_TOKEN"])
#
# input = {
#     "garm_img": "https://yisol-idm-vton.hf.space/file=/tmp/gradio/97168750c1cb1570a41d299e14df6a6f0ea12fda/09236_00.jpg",
#     "human_img": "https://yisol-idm-vton.hf.space/file=/tmp/gradio/50030d57a9fbbd6a1679ea75111bee036bdcec3a/01992_00.jpg",
#     "garment_des": "cute pink top"
# }
#
# output = api.run(
#     "cuuupid/idm-vton:906425dbca90663ff5427624839572cc56ea7d380343d13e2a4c4b09d3f0c30f",
#     input=input
# )
# print(output)
# #=> "https://replicate.delivery/pbxt/Tfs5JETdzlURKyKeUOltKwch...