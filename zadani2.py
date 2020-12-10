#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a = {1: "один", 2: "два", 3: "три", 4: "четыре", 5: "пять", }
    new_a = {j: i for i, j in a.items()}
    print(f'{a}', f'{new_a}', sep='\n')