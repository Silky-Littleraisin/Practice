#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# テキスト中の品詞のn-gramを数える
#
import sys
from collections import Counter
import MeCab

ngram = 3
mecab = MeCab.Tagger("-Ochasen")


## 形態素解析(品詞だけ数える)
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


def main():
    with open(sys.argv[1]) as f:
        text = f.read()
        poses = mecab_tokenizer(text)

    total_pos = len(poses)
    ngram_poses = []
    for i, pos in enumerate(poses):
        if i + ngram > total_pos:
            break
        ngram_pos = '-'.join(poses[i:i + ngram])
        ngram_poses.append(ngram_pos)

    count = Counter(ngram_poses)
    sorted_ngram = sorted(count.items(), key=lambda x: -x[1])
    print(sorted_ngram[:20])


if __name__ == '__main__':
    main()