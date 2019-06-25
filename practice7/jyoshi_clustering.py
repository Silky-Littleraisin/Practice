#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 助詞の出現割合を使用して小説をボトムアップクラスタリングする
#
import sys
import os
import re
import pathlib
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from scipy.cluster.hierarchy import linkage, dendrogram
import umap
import MeCab

mecab = MeCab.Tagger("-Ochasen")
plt.rcParams['font.family'] = "IPAexGothic"

## 形態素解析
def mecab_tokenizer(text):
    word_list = list()

    node = mecab.parseToNode(text)
    while node:
        if node.surface != "":
            res = node.feature.split(",")
            if node.surface not in ['(', ')', '-', '+', '"'] and \
               res[0] in ["助詞"] and \
               res[1] not in ["副助詞", '終助詞', '副助詞／並立助詞／終助詞', '接続助詞']:
                word_list.append(node.surface)

        node = node.next
    return word_list

## 助詞を数える
def count_word(file):
    with open(file) as f:
        text = f.read()
        words = mecab_tokenizer(text)

    count = Counter(words)
    return count, len(words)

# デンドログラムを描画する
def show_dendrogram(matrix, analized):
    z = linkage(matrix, method='ward', metric = 'euclidean')
    dendrogram(z, labels=list(analized.keys()), leaf_rotation=90)
    plt.tight_layout()
    plt.show()

def show_umap(matrix, analized):
    embedding = umap.UMAP().fit_transform(matrix)
    fig, ax = plt.subplots()
    ax.scatter(embedding[:,0], embedding[:,1], cmap=cm.tab10)

    titles = list(analized.keys())
    for i, val in enumerate(embedding):
        ax.annotate(titles[i], xy=(val[0], val[1]), size=10)
    plt.show()

def main():
    analized = {}
    # dataにある.sentファイルをすべて読み込む
    data_path = pathlib.Path('./data')
    for filename in data_path.glob('*.sent'):
        title = re.sub('data/(.+?).sent', '\\1', str(filename))
        analized[title] = count_word(filename)
        print("finish:", title, file=sys.stderr)

    word_total = {}
    for count, num in analized.values():
        for w, freq in count.items():
            if w not in word_total:
                word_total[w] = 0
            word_total[w] += freq

    # 助詞を頻出順に並べる
    frequent_word = sorted(word_total.items(), key=lambda x: -x[1])

    matrix = []
    for title, value in analized.items():
        row = []
        for w in frequent_word[:5]:   # 助詞の上位5語だけを使う
            # 小説全体の長さで割って、正規化する
            row.append( value[0][w[0]] / value[1] )
        matrix.append(row)

    #show_dendrogram(matrix, analized)
    show_umap(matrix, analized)


if __name__ == '__main__':
    main()