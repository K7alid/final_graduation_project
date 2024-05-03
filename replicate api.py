import replicate


import os
import replicate

#Set the REPLICATE_API_TOKEN environment variable
os.environ["REPLICATE_API_TOKEN"] = "r8_buLTfoRw7E7A32AIPDteMYnrmZZPVrk3KgkJb"
api = replicate.Client(api_token=os.environ["REPLICATE_API_TOKEN"])

input = {
    "garm_img": "https://yisol-idm-vton.hf.space/file=/tmp/gradio/97168750c1cb1570a41d299e14df6a6f0ea12fda/09236_00.jpg",
    "human_img": "https://yisol-idm-vton.hf.space/file=/tmp/gradio/50030d57a9fbbd6a1679ea75111bee036bdcec3a/01992_00.jpg",
    "garment_des": "cute pink top"
}

output = api.run(
    "cuuupid/idm-vton:906425dbca90663ff5427624839572cc56ea7d380343d13e2a4c4b09d3f0c30f",
    input=input
)
print(output)
#=> "https://replicate.delivery/pbxt/Tfs5JETdzlURKyKeUOltKwch...