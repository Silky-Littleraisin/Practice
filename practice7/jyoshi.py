#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# テキスト中の助詞の頻度を数える
#
import sys
from collections import Counter
import MeCab

mecab = MeCab.Tagger("-Ochasen")


## 形態素解析(助詞だけ保存する)
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


def main():
    with open(sys.argv[1]) as f:
        text = f.read()
        words = mecab_tokenizer(text)

    # 助詞を数える
    count = Counter(words)
    print(count)


if __name__ == '__main__':
    main()