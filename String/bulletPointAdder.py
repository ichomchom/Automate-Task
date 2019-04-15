#! /usr/bin/env python3
# bulletPoitnAdder.py -  Adds wikipedia bullet pionts to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

# separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)): #loop through all index in the "lines" list
	lines[i] = '* ' + lines[i] # add star to each string in "lines" list

text = '\n'.join(lines)

pyperclip.copy(text)

