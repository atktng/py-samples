#!/usr/bin/env python3

import csv
from random import choice, randint
import sys


def get_substr_word(wl: list, len: int) -> str:
    return choice(wl)[:len]

def get_prefix_word(wl: list, len: int) -> str:
    return wl[0][:len]

def get_suffix_word(wl: list, len: int) -> str:
    return wl[-1][-len:]

if len(sys.argv) != 2:
    print('Usage: ./gen_rand_str_from_csv.py <csvpath>')
    sys.exit()

with open(sys.argv[1]) as f:
    rd = csv.reader(f)
    m = [row for row in rd]

for i in range(10):
    wl = [choice(r) for r in m]

    # Join
    words = ' '.join(wl)
    print(words)

    # Get substring
    print(get_substr_word(wl, randint(1, 5)))
    print(get_prefix_word(wl, randint(1, 5)))
    print(get_suffix_word(wl, randint(1, 5)))
