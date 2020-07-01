#!/usr/bin/env python3

import csv
from random import choice


with open('words.csv') as f:
    rd = csv.reader(f)
    m = [row for row in rd]

for i in range(1000):
    print(''.join([choice(r) for r in m]))
