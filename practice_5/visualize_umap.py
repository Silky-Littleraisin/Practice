#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#
import sys
import os
import MeCab
import numpy as np
import matplotlib.pyplot as plt
import umap
import seaborn as sns
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from scipy.sparse.csgraph import connected_components

DIRS = ['dokujo-tsushin', 'movie-enter', 'it-life-hack']
tagger = MeCab.Tagger("-Ochasen")
sns.set()

# 形態素解析の関数化
def mecab_tokenizer(text):
    word_list = list()
    node = tagger.parseToNode(text)
    while node:
        if node.surface != "":
            res = node.feature.split(",")
            if node.surface not in ['(', ')', '-', '+', '"'] and \
               res[0] in ["名詞", "動詞", "形容詞", "副詞"] and \
               res[1] not in ["数", '記号', '非自立', '接尾']:
                basic_word = res[6] if res[6] != "*" else node.surface
                word_list.append(basic_word)

        node = node.next
    return word_list

def main():
    # 単なる単語頻度によるベクトル化
    vectorizer = CountVectorizer(tokenizer=mecab_tokenizer)

    # tf-idfベクトル化変数(正規化はL2, tfにlogを用いる)
    # vectorizer = TfidfVectorizer(norm='l2', sublinear_tf=True,
    #                             tokenizer=mecab_tokenizer)

    text_list = []
    dir_list = []
    for d in DIRS:
        # ファイルリストから'LICENSE.txt'を除く
        files = [f for f in os.listdir("text/" + d) if f != 'LICENSE.txt']
        # カテゴリごとに10ファイルずつ
        for fi in files[:10]:
            with open('text/{}/{}'.format(d, fi)) as f:
                lines = f.readlines()
                text_list.append("".join(lines[3:]))
                dir_list.append(d)

    # テキストデータのベクトル化
    weighted_matrix = vectorizer.fit_transform(text_list)
    # umapによる次元削減
    embedding = umap.UMAP().fit_transform(weighted_matrix.toarray())

    # seabornでの描画のためにpandasのDataFrameに結果を変換
    df = pd.DataFrame()
    df['x'] = embedding[:,0]
    df['y'] = embedding[:,1]
    df['label'] = dir_list
    # 散布図を描画
    sns.lmplot('x', 'y', data=df, hue="label", fit_reg=False)
    plt.show()

if __name__ == '__main__':
    main()