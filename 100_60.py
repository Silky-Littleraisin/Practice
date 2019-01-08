﻿# coding: utf-8
import gzip
import json
import leveldb

fname = 'artist.json.gz'
fname_db = 'test_db'

# LevelDBオープン、なければ作成
db = leveldb.DB(bytes("/Users/silky/Documents/GitHub/Practice/level_test", "ascii"),create_if_missing=True)

# gzファイル読み込み、パース
with gzip.open(fname, 'rt') as data_file:
    for line in data_file:
        data_json = json.loads(line)

        # key=name+id、value=areaとしてDBへ追加
        key = data_json['name'] + '\t' + str(data_json['id'])
        value = data_json.get('area', '')       
# areaはないことがある
        db.put(key.encode(), value.encode())


# 確認のため登録件数を表示
print('{}件登録しました。'.format(len(list(db.keys()))))