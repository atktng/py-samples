#!/usr/bin/env python3

import csv
from random import choice
import sys


if len(sys.argv) != 2:
    print('Usage: ./gen_rand_str_from_csv.py <csvpath>')
    sys.exit()

with open(sys.argv[1]) as f:
    rd = csv.reader(f)
    m = [row for row in rd]

for i in range(1000):
    print(' '.join([choice(r) for r in m]))
