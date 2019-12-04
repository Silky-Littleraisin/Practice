#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Google Computer Vision Document Text Detection API
#
import sys
import requests
import json
import base64

# 実際に使用するときは独自のAPI_KEYを取得すること
API_KEY = "AIzaSyAikdAcQfppWqo3BMmx8Oc2Bl83i21aXhc"
api_url = 'https://vision.googleapis.com/v1/images:annotate?key={}'.format(API_KEY)

# 画像ファイルを読み込み、base64文字列に変換する
img_path = '956586-025.jpg'
with open(img_path, "rb") as img:
    image_content = base64.b64encode(img.read())

# 画像データを含んだJSONデータを生成する
req_body = json.dumps({
    'requests': [{
        'image': {
            'content': image_content.decode('utf-8')
        },
        'features': [{
            'type': 'DOCUMENT_TEXT_DETECTION'
        }]
    }]
})

# APIにデータを送り、レスポンスを受け取る
res = requests.post(api_url, data=req_body)
res_json = res.json()

with open('Google/956586-025.json','w') as obj:
    obj.writelines(json.dumps(res_json, ensure_ascii=False))

print(json.dumps(res_json, ensure_ascii=False))