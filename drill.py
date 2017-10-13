#!/usr/bin/python3

import sys
from random import choice

drill_seq = sys.argv[1:]

# "barely enough" parsing for -b
if drill_seq[0] == "-b":
    drill_seq.remove("-b")
    printBeginP = True
else:
    printBeginP = False

while True:
    live_seq = drill_seq[:]

    if printBeginP:
        print("(start of new sequence)")

    while live_seq:
        nxt = choice(live_seq)
        print(nxt)
        live_seq.remove(nxt)

        print("press enter for next item")
        input()
