#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# MS Azure Compouter Vision OCR API
#
import sys
import requests
import json

# 実際に使用するときは独自のSubscription Keyを取得すること
subscription_key = "96b0ed201512488f8258279f7a007deb"
ocr_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v2.0/ocr"

# 画像ファイルの読み込み
file_name = sys.argv[1]
file_data = open(file_name, 'rb').read()

# APIに送るパラメーター
files = {'uploadFile': (file_name, file_data, 'image/jpeg')}
headers = {'Ocp-Apim-Subscription-Key': subscription_key}
params  = {'language': 'unk', 'detectOrientation': 'true'}

response = requests.post(ocr_url, headers=headers, params=params, files=files)
response.raise_for_status()

analysis = response.json()
print(json.dumps(analysis, ensure_ascii=False))
