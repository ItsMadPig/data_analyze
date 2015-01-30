#!/usr/bin/env python

import sys

current_word = None
current_count = 0
word = None
date = None

for line in sys.stdin:
	line = line.strip()
	word, date, count = line.split('\t')
	
	try:
		count = int(count)
	except ValueError:
		continue

	if current_word == word:
		current_count+= count
	else:
		if current_word:
			if current_count > 100000:
				print '%s\t%s%s' %(current_count,current_word,current_outline)
		current_count = count
		current_word = word
		current_outline = ""
		for x in range(1,31):
			current_outline += "\t"+ "201411" + str(x).rjust(2,'0')+":0"
	idx1 = current_outline.index(date)
	idx2 = current_outline.index(":",idx1+1)
	try:
		idx3 = current_outline.index("\t",idx1+1)
		c = int(current_outline[idx2+1:idx3])
		current_outline = current_outline[:idx2+1] + str(c+count)+ current_outline[idx3:]
	except ValueError:
		idx3 = len(current_outline)
		c = int(current_outline[idx2+1:idx3])
		current_outline = current_outline[:idx2+1] + str(c+count)

	#current_outline = current_outline.replace((date+":0"),(date+':'+str(count)))
if current_word == word:
	if current_count > 100000:
		print '%s\t%s%s' %(current_count,current_word,current_outline)

