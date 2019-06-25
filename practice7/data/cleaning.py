#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 青空文庫テキストファイルからルビなどを削除して、1行1文のテキストファイルにする
#
import sys
import re
import codecs

cnt = 0
f = codecs.open(sys.argv[1], "r", "shift_jis")
line = f.readline()
while line:
    if re.match('底本', line):
        break;
    if re.match('----', line):
        cnt += 1
        line = f.readline()
        continue
    if cnt < 2:
        line = f.readline()
        continue
    line = line.strip()
    line = re.sub('\x0d$', '', line)
    line = re.sub('｜', '', line)
    line = re.sub('《[^《]*?》|［＃[^［]*?］|〔[^〔]*?〕', '', line)
    line = re.sub('^　', '', line)
    if re.match('\s*$', line):
        line = f.readline()
        continue
    line = re.sub('(。)', '\\1\n', line)
    line = re.sub('(」)(「)', '\\1\n\\2', line)
    sentences = [ l for l in re.split('\n+', line) if not re.match('\s*$', line) ]
    print('\n'.join(sentences))
    line = f.readline()