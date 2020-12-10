#!/usr/bin/env python 3
# -*- config: utf-8 -*-

if __name__ == '__main__':
    school = {'1а': 25, '1б': 27, '2а': 22, '2б': 24,  '3а': 25, '3б': 27,  '4а': 25, '4б': 27, '5а': 25, '5б': 27,  '6а': 25, '6б': 27,  '7а': 25, '7б': 27,  '8а': 25, '8б': 27,  '9а': 25, '9б': 27,  '10а': 25, '10б': 27, '11а': 25, }

    school['11а'] = 15
    school['11б'] = 11
    del school['8б']

    pupils = 0
    for i, j in enumerate(school):
        pupils += school[j]
        print(j, ":", school[j])
    print(f"Общее число учащихся в школе: {pupils}")