#!/usr/bin/env python2

import os
import datetime
import argparse

# parse script arguments
parser = argparse.ArgumentParser()
parser.add_argument('msg', help="output message")
args = parser.parse_args()

# assign runtime variables
msg  = ''.join(map(str.upper, args.msg))
cron = "00 12 {day:2} {month:2} * {path} 20"
path = os.path.join(os.getcwd(), 'gh-print.sh')
date = datetime.date.today()

# define character matrix
matrix = {
    # punctuation
    ' ': [
        (0, 0, 0, 0, 0, 0, 0)
    ],
    '.': [
        (0, 0, 0, 0, 0, 1, 0)
    ],
    '!': [
        (0, 1, 1, 1, 0, 1, 0)
    ],
    # '?': [],

    # numerals
    # '0': [],
    # '1': [],
    # '2': [],
    # '3': [],
    # '4': [],
    # '5': [],
    # '6': [],
    # '7': [],
    # '8': [],
    # '9': [],
    
    # alpha
    # 'A': [],
    # 'B': [],
    # 'C': [],
    'D': [
        (0, 1, 1, 1, 1, 1, 0),
        (0, 1, 0, 0, 0, 1, 0),
        (0, 1, 0, 0, 0, 1, 0),
        (0, 0, 1, 1, 1, 0, 0)
    ],
    'E': [
        (0, 1, 1, 1, 1, 1, 0),
        (0, 1, 0, 1, 0, 1, 0),
        (0, 1, 0, 1, 0, 1, 0),
        (0, 1, 0, 1, 0, 1, 0)
    ],
    # 'F': [],
    # 'G': [],
    'H': [
        (0, 1, 1, 1, 1, 1, 0),
        (0, 0, 0, 1, 0, 0, 0),
        (0, 0, 0, 1, 0, 0, 0),
        (0, 1, 1, 1, 1, 1, 0)
    ],
    # 'I': [],
    # 'J': [],
    # 'K': [],
    'L': [
        (0, 1, 1, 1, 1, 1, 0),
        (0, 0, 0, 0, 0, 1, 0),
        (0, 0, 0, 0, 0, 1, 0),
        (0, 0, 0, 0, 0, 1, 0)
    ],
    # 'M': [],
    # 'N': [],
    'O': [
        (0, 0, 1, 1, 1, 0, 0),
        (0, 1, 0, 0, 0, 1, 0),
        (0, 1, 0, 0, 0, 1, 0),
        (0, 0, 1, 1, 1, 0, 0)
    ],
    # 'P': [],
    # 'Q': [],
    'R': [
        (0, 1, 1, 1, 1, 1, 0),
        (0, 1, 0, 1, 0, 0, 0),
        (0, 1, 0, 1, 0, 0, 0),
        (0, 0, 1, 0, 1, 1, 0)
    ],
    # 'S': [],
    # 'T: [],
    # 'U': [],
    # 'V': [],
    'W': [
        (0, 1, 1, 1, 1, 0, 0),
        (0, 0, 0, 0, 0, 1, 0),
        (0, 0, 1, 1, 1, 0, 0),
        (0, 0, 0, 0, 0, 1, 0),
        (0, 1, 1, 1, 1, 0, 0)
    ],
    # 'X': [],
    'Y': [
        (0, 1, 0, 0, 0, 0, 0),
        (0, 0, 1, 0, 0, 0, 0),
        (0, 0, 0, 1, 1, 1, 0),
        (0, 0, 1, 0, 0, 0, 0),
        (0, 1, 0, 0, 0, 0, 0)
    ]
    # 'Y': [],
    # 'Z': []
}

# determine starting monday
if date.weekday():
    days = 0 - date.weekday()
    if days <= 0: days += 7
    date += datetime.timedelta(days)

# output cron tab
print "# gh-print '%s' begin" % msg
for ch in msg:
    print "# gh-print character '%s'" % ch
    if ch not in matrix: continue
    for week in matrix[ch]:
        for bit in week:
            day, month = date.day, date.month
            if bit: print cron.format(**locals())
            date += datetime.timedelta(1)
print "# gh-print '%s' end" % msg
