#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#
import sys
import os
import MeCab
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from scipy.cluster.hierarchy import linkage, dendrogram

DIRS = ['dokujo-tsushin', 'movie-enter', 'it-life-hack']
mecab = MeCab.Tagger("-Ochasen")

def mecab_tokenizer(text):
    word_list = list()

    node = mecab.parseToNode(text)
    while node:
        if node.surface != "":
            res = node.feature.split(",")
            if node.surface not in ['(', ')', '-', '+', '"'] and \
               res[0] in ["名詞", "動詞", "形容詞", "副詞"] and \
               res[1] not in ["数", '記号', '非自立']:
                basic_word = res[6] if res[6] != "*" else node.surface
                word_list.append(basic_word)

        node = node.next
    return word_list

def main():
    # 単なる単語頻度によるベクトル化
    vectorizer = CountVectorizer(tokenizer=mecab_tokenizer)

    # tf-idfベクトル化変数(正規化はL2, tfにlogを用いる)
    # vectorizer = TfidfVectorizer(norm='l2', sublinear_tf=True,
    #                              tokenizer=mecab_tokenizer)

    text_list = []
    id_list = []
    #for d in DIRS:
    for i in range(1):
        files = [f for f in os.listdir("news") if f != 'get_nes.py']
        for fi in files[:10]:
            with open('news/{}'.format(fi)) as f:
                lines = f.readlines()
                text_list.append("".join(lines[3:]))
                id_list.append(fi.split('.')[0])

    weighted_matrix = vectorizer.fit_transform(text_list)

    # 階層的クラスタリングをする
    # クラスタリング手法(method), 距離関数(metrics)の種類
    # methods = ["single", "complete", "average", "weighted",
    #            "centroid", "median", "ward"]
    # metrics = ['braycurtis', 'canberra', 'chebyshev', 'cityblock',
    #            'correlation', 'cosine', 'euclidean', 'hamming', 'jaccard']
    z = linkage(weighted_matrix.toarray(), method='ward', metric = 'euclidean')
    # デンドログラムを描画する
    dendrogram(z, labels=id_list, leaf_rotation=90)
    plt.tight_layout()
    # 表示
    plt.show()

if __name__ == '__main__':
    main()