hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.find('Form:') >= 0:
        print(line)

import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('Form:', line):
        print(line)