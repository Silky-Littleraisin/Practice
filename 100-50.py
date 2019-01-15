# coding utf-8
import re

fname = 'nlp.txt'

def nlp_lines():

    ''' nlp を1文ずつ読み込むジェネレータ
    nlp.txtを順次読み込んで1文ずつ返す
    '''


    with open(fname) as lines:
        pattern = re.compile(r'''
        (^
        .*?
        [\.|;|:|\?|!]
        )
        \s
        (
            [A-Z].*
        )
        ''',re.MULTILINE+re.VERBOSE + re.DOTALL)

        for line in lines:
            line = line.strip()
            while len(line) > 0:

                match= pattern.match(line)
                if match:

                    yield match.group(1)

                    line=match.group(2)

                else:
                    yield line
                    line=''
for line in nlp_lines():
    print (line)
