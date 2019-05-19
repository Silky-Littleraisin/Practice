#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#
import sys
from newspaper import Article

url = sys.argv[1]
a = Article(url)
print(url, file=sys.stderr)
a.download()
a.parse()
print("Title: ", a.title) # 記事のタイトル
print("Body: ", a.text)   # 記事の本文
