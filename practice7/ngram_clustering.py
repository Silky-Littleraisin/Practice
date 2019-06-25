#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 品詞のn-gramの出現割合を使用して小説をボトムアップクラスタリングする
#
import sys
import os
import re
import pathlib
from collections import Counter
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from scipy.cluster.hierarchy import linkage, dendrogram
import umap
import MeCab

ngram = 2
mecab = MeCab.Tagger("-Ochasen")
plt.rcParams['font.family'] = "IPAexGothic"


## 形態素解析
def mecab_tokenizer(text):
    pos_list = list()
    node = mecab.parseToNode(text)
    while node:
        pos = ''
        if node.surface == "EOS":
            pos = node.surface
        else:
            res = node.feature.split(",")
            pos = res[0]
        pos_list.append(pos)
        node = node.next
    return pos_list


def count_ngram(file):
    with open(file) as f:
        text = f.read()
        poses = mecab_tokenizer(text)

    total_pos = len(poses)
    ngram_poses = []
    for i, pos in enumerate(poses):
        if i + ngram < total_pos:
            ngram_pos = '-'.join(poses[i:i + ngram])
            ngram_poses.append(ngram_pos)

    count = Counter(ngram_poses)
    return (count, total_pos)


# デンドログラムを描画する
def show_dendrogram(matrix, analized):
    z = linkage(matrix, method='ward', metric='euclidean')
    dendrogram(z, labels=list(analized.keys()), leaf_rotation=90)
    plt.tight_layout()
    plt.show()


def show_umap(matrix, analized):
    embedding = umap.UMAP().fit_transform(matrix)
    fig, ax = plt.subplots()
    ax.scatter(embedding[:, 0], embedding[:, 1], cmap=cm.tab10)

    titles = list(analized.keys())
    for i, val in enumerate(embedding):
        ax.annotate(titles[i], xy=(val[0], val[1]), size=10)
    plt.show()


def main():
    analized = {}
    data_path = pathlib.Path('./data')
    for filename in data_path.glob('*.sent'):
        title = re.sub('data/(.+?).sent', '\\1', str(filename))
        analized[title] = count_ngram(filename)
        print("finish:", title, file=sys.stderr)

    ngram_sum = {}
    for count, num in analized.values():
        for n, freq in count.items():
            if n not in ngram_sum:
                ngram_sum[n] = 0
            ngram_sum[n] += freq

    frequent_ngram = sorted(ngram_sum.items(), key=lambda x: -x[1])

    matrix = []
    for title, value in analized.items():
        row = []
        for n in frequent_ngram[:100]:
            # 小説全体の長さで割って、正規化する
            row.append(value[0][n[0]] / value[1])
        matrix.append(row)

    #show_dendrogram(matrix, analized)
    show_umap(matrix, analized)


if __name__ == '__main__':
    main()