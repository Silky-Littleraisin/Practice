#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#
import sys
import os
import MeCab
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.cluster import KMeans

DIRS = ['dokujo-tsushin', 'movie-enter', 'it-life-hack']
tagger = MeCab.Tagger("-Ochasen")


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
    #                              tokenizer=mecab_tokenizer)

    text_list = []
    id_list = []
    for d in DIRS:
        # ファイルリストから'LICENSE.txt'を除く
        files = [f for f in os.listdir("text/" + d) if f != 'LICENSE.txt']
        # カテゴリごとに10ファイルずつ
        for fi in files[:10]:
            with open('text/{}/{}'.format(d, fi)) as f:
                lines = f.readlines()
                text_list.append("".join(lines[3:]))
                id_list.append(fi.split('.')[0])

    # テキストデータのベクトル化
    weighted_matrix = vectorizer.fit_transform(text_list)

    # ベクトル情報を確認
    print("テキスト数:%d,単語の種類数:%d" % weighted_matrix.shape)

    # k-meansの実行
    cluster = KMeans(n_clusters=3).fit_predict(weighted_matrix)

    ## 出力用のデータ編集
    index = weighted_matrix.toarray().argsort(axis=1)[:, ::-1]
    features = np.array(vectorizer.get_feature_names())
    feature_words = features[index]

    # 出力単語の数
    num_words = 5
    print("クラスタ\tファイル名\ttf-idf値の高い単語")
    for cl, name, fwords in zip(cluster, id_list, feature_words[:, :num_words]):
        print("{}\t{}\t{}".format(cl, name, fwords))


if __name__ == '__main__':
    main()