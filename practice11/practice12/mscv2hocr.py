#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Translate MS Azure Computer Vision OCR API Output to hocr format
#                                          2019, Takeshi Abekawa
#
import sys
import json
import html

with open(sys.argv[1]) as f:
    json = json.loads(f.read())

rows = []
for block in json['regions']:
    for line in block['lines']:
        xmin, ymin, w, h = line['boundingBox'].split(',')
        rows.append({
            'xmin': int(xmin),
            'ymin': int(ymin), 
            'xmax': int(xmin) + int(w),
            'ymax': int(ymin) + int(h),
            'text': "".join([ word['text'] for word in line['words'] ])
        })

min_x = min([ r['xmax'] for r in rows ])
min_y = min([ r['ymax'] for r in rows ])
max_x = max([ r['xmax'] for r in rows ])
max_y = max([ r['ymax'] for r in rows ])

print('''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="unknown" lang="unknown">
  <head>
    <title>None</title>
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
    <meta name='ocr-system' content='ms2hocr.py' />
    <meta name='ocr-langs' content='unknown' />
    <meta name='ocr-number-of-pages' content='1' />
    <meta name='ocr-capabilities' content='ocr_page ocr_carea ocr_line ocrx_word ocrp_lang'/>
  </head>
  <body>''')

print("    <div class='ocr_page' lang='unknown' title='bbox 0 0 {0} {1}'>".format(max_x, max_y))
print("      <div class='ocr_carea' lang='unknown' title='bbox {0} {1} {2} {3}'>".format(min_x, min_y, max_x, max_y))

for i, r in enumerate(rows):
    print("        <span class='ocr_line' id='line_{0}' title='bbox {1} {2} {3} {4}; baseline 0 -5'>".format(i, r['xmin'], r['ymin'], r['xmax'], r['ymax']))
    print("          <span class='ocrx_word' id='word_{0}_0' title='bbox {1} {2} {3} {4}'>{5}</span>".format(i, r['xmin'], r['ymin'], r['xmax'], r['ymax'], html.escape(r['text'], quote=True)))
    print("        </span>")

print("      </div>\n    </div>\n  </body>\n</html>\n")
