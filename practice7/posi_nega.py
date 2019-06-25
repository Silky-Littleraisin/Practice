#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# テキストファイルから評価表現を取り出す
#
import sys
import csv
import MeCab

mecab = MeCab.Tagger("-Ochasen")

## 辞書の読み込み
def read_dict():
    pn_dic = {}
    with open('wago.121808.pn', "r") as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            if len(row) < 2:
                continue
            value, phrase = row[0], row[1]
            pn_dic[phrase] = value
    return pn_dic

## 形態素解析
def mecab_tokenizer(text):
    word_list = []
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
    # 評価極性辞書の読み込み
    pn_dic = read_dict()
    # テキストの読み込みと解析
    with open(sys.argv[1]) as f:
        text = f.read()
        words = mecab_tokenizer(text)

    n = len(words)
    for i in range(0, n):
        # 10フレーズまで確認
        for k in range(10, 0, -1):
            if i+k > n - 1:
                continue
            # フレーズを作成
            phrase = ' '.join(words[i:i+k])
            # 辞書にあれば出力
            if phrase in pn_dic:
                print(pn_dic[phrase], "\t", phrase)
                break

if __name__ == '__main__':
    main()