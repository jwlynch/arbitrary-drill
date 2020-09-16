#!/usr/bin/python3

import subprocess

keys = \
    [
        "A",
        "Bb",
        "B",
        "C",
        "D",
        "Eb",
        "E",
        "F",
        "F#",
        "G",
        "Ab",
    ]

argArray = ["python3", "drill.py"] + keys

subprocess.run(argArray)
