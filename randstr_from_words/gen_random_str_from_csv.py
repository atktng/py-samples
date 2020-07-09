#!/usr/bin/env python3

import csv
from random import choice
import sys


def get_substr_word(word: str, len: int) -> str:
    return choice(word.split(" "))[:len]

def get_prefix_word(word: str, len, int) -> str:
    return word.sprit(" ")[0][:len]

if len(sys.argv) != 2:
    print('Usage: ./gen_rand_str_from_csv.py <csvpath>')
    sys.exit()

with open(sys.argv[1]) as f:
    rd = csv.reader(f)
    m = [row for row in rd]

for i in range(10):
    word = ' '.join([choice(r) for r in m])
    print(word)

    print(get_substr_word(word, 3))
