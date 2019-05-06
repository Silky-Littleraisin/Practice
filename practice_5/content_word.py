#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
import sys
import MeCab

# MeCabの準備
tagger = MeCab.Tagger("-Ochasen")

with open(sys.argv[1]) as f:
    # テキスト全部を読み込む
    lines = f.readlines()
    # 本文は3行目以降、行を連結して1つの文字列に
    text = "".join(lines[3:])
    # 結果を格納する配列
    word_list = []
    # MeCabで形態素解析、1形態素ごとに結果がnodeに入る
    node = tagger.parseToNode(text)
    while node:
        if node.surface != "": # 表層形が空文字列でないとき
            # 品詞を","で分割
            res = node.feature.split(",")
            # 表層形や品詞が次のような条件のとき
            if node.surface not in ['(', ')', '-', '+', '"'] and \
               res[0] in ["名詞", "動詞", "形容詞", "副詞"] and \
               res[1] not in ["数", '記号', '非自立', '接尾']:
                # 一般語は基本形、固有名詞は表層形
                basic_word = res[6] if res[6] != "*" else node.surface
                # 配列に入れる
                word_list.append(basic_word)
        # 次の形態素へ
        node = node.next

    # 最後に配列を出力
    print(word_list)