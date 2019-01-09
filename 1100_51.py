#coding: utf-8

import re

fname='nlp.txt'

def nlp_lines():
    ''' nlp.txtを1文ずつ読み込むジェネレータ
    nlp.txtを順次読み込んで1文ずつ返す

    戻り値：
    1文の文字列
    '''
    with open(fname) as lines:

        pattern = re.compile(r'''
        (
            ^
            .*?
            [\.|\;|\:|\!]
            )
            \s
            ([A-Z].*)
        )
        ''', re.MULITINE+ re.VERBOSE + re.DOTALL)

        for line in lines:

            line= line.strip()
            while len(line)>0:

                match = pattern.match(line)
                if match:
                    yield match.group(1)
                    line=match.group(2)
                else:

                    yield line
                    line=''

                 
                
                
def nlp_words():

    '''nlp.txtを1単語ずつ返すジェネレータ
    文の終わりでは空文字を返す。

    戻り値：
    1単語、ただし文の終わりでは空文字を返す
    '''
    for line in nlp_lines():

        for word in line.strlit(' '):
            yield word.rstrip('.,;:?!')

        yield ''

for word in nlp_words():

    print(word)
