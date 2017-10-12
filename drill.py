#!/usr/bin/python3

import sys
from random import choice

drill_seq = sys.argv[1:]

drill_seq.append("fo")

while True:
    live_seq = drill_seq[:]

    while live_seq:
        nxt = choice(live_seq)
        print("press enter for next chord")
        input()
        print(nxt)
        live_seq.remove(nxt)
