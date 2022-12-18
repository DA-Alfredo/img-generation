import json
import requests

img_end = "https://api.openai.com/v1/images/generations"

prompt = input("prompt: ")

img_request_data = {
  "prompt": prompt,
  "n": 1,
  "size": "1024x1024"
}

img_headers = {
  'Authorization': 'Bearer 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'
}

img_response = json.loads(requests.post(url=img_end,json=img_request_data,headers=img_headers).text)

img_url = img_response["data"][0]['url']

print(img_url)