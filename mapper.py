#!/usr/bin/env python

import sys
import os

fname=os.environ["mapreduce_map_input_file"]
idx1=fname.find("pagecounts-")

for line in sys.stdin:
	line = line.strip()
	words = line.split()
	if (len(words)!= 4):
		continue
	
	if (words[0]!="en"):
		continue
	
	if ((words[1][:6]=="Media:") or
		(words[1][:8]=="Special:") or
		(words[1][:5]=="Talk:") or
		(words[1][:5]=="User:") or
		(words[1][:10]=="User_talk:") or
		(words[1][:8]=="Project:") or
		(words[1][:13]=="Project_talk:") or
		(words[1][:5]=="File:") or
		(words[1][:10]=="File_talk:") or
		(words[1][:10]=="MediaWiki:") or
		(words[1][:15]=="MediaWiki_talk:") or
		(words[1][:9]=="Template:") or
		(words[1][:14]=="Template_talk:") or
		(words[1][:5]=="Help:") or
		(words[1][:10]=="Help_talk:") or
		(words[1][:9]=="Category:") or
		(words[1][:14]=="Category_talk:") or
		(words[1][:7]=="Portal:") or
		(words[1][:10]=="Wikipedia:") or
		(words[1][:15]=="Wikipedia_talk:")):
		continue

	if (words[1][0]).islower():
		continue
	length = len(words[1])
	if (((words[1][length-4:])==".jpg")or
		((words[1][length-4:])==".gif")or
		((words[1][length-4:])==".png")or
		((words[1][length-4:])==".JPG")or
		((words[1][length-4:])==".GIF")or
		((words[1][length-4:])==".PNG")or
		((words[1][length-4:])==".txt")or
		((words[1][length-4:])==".ico")):
		continue

	if ((words[1]=="404_error/")or
		(words[1]=="Main_Page")or
		(words[1]=="Hypertext_Transfer_Protocol")or
		(words[1]=="Search")):
		continue

	print "%s\t%s\t%s" % (words[1],fname[idx1+11:idx1+19],words[2])
