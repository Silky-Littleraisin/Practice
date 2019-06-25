#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
import sys
import os
import MeCab
import re
import csv
import math
import matplotlib.pyplot as plt

segment_size = 2000
window_size = 5
mecab = MeCab.Tagger("-Ochasen")

## 辞書の読み込み(ポジ:1, ネガ:-1)
def read_dict():
    pn_dic = {}
    with open('wago.121808.pn', "r") as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            if len(row) < 2:
                continue
            value, phrase = row[0], row[1]
            pn_dic[phrase] = 1 if value[0:2] == 'ポジ' else -1
    return pn_dic

## 形態素解析
def mecab_tokenizer(text):
    word_list = list()
    node = mecab.parseToNode(text)
    while node:
        if node.surface != "":
            res = node.feature.split(",")
            # 単語の原形を使う
            basic_word = res[6] if res[6] != "*" else node.surface
            word_list.append(basic_word)
        node = node.next
    return word_list

def main():
    pn_dic = read_dict()
    # テキストの読み込みと解析
    with open(sys.argv[1]) as f:
        text = f.read()
        words = mecab_tokenizer(text)

    n = len(words)
    segment_num = math.floor(n/segment_size) - window_size
    print("長さ:", n, "セグメント数:", segment_num, file=sys.stderr)
    # 長さチェック
    if n < 14000:
        print("too small to calculate:", n)
        sys.exit()

    data = []
    for i in range(0, segment_num):
        emotion = 0
        emotion_word_num = 0
        start = i * segment_size
        # window_size内の単語すべて
        for j in range(start, start+segment_size*window_size):
            # 10形態素のフレーズまで確認
            for k in range(10, 0, -1):
                if j+k > n - 1:
                    continue
                # フレーズを作成
                phrase = ' '.join(words[j:j+k])
                if phrase in pn_dic:
                    value = pn_dic[phrase]
                    # print(phrase, value)
                    emotion += value
                    emotion_word_num += 1
                    break

        # セグメントの評価値平均を計算
        average = emotion/emotion_word_num if emotion_word_num > 0 else 0
        data.append(average)

    # 折れ線グラフを描画
    plt.ylim(-0.5, 0.5)
    plt.plot(
        list(range(0, len(data))),
        data
    )
    plt.show()

if __name__ == '__main__':
    main()