#!/usr/bin/python3

import sys
from random import choice

def usage(progname):
    print("%s: Usage:" % progname)
    print("%s" % progname)
    print("%s (to print this usage message)" % (" " * len(progname)))

def main(progname=None, args=None):
    if progname is None:
        progname = "prog"


# "barely enough" parsing for -b
if drill_seq[0] == "-b":
    drill_seq.remove("-b")
    printBeginP = True
else:
    printBeginP = False

input("press enter for next item: ")

while True:
    live_seq = drill_seq[:]

    if printBeginP:
        print("(start of new sequence)")

    while live_seq:
        nxt = choice(live_seq)
        print(nxt)
        live_seq.remove(nxt)

        input("press enter for next item: ")
