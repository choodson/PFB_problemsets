#!/usr/bin/env python3

import sys
sam_file = open(sys.argv[1],"r")
read=[]
transcript=[]
for line in sam_file:
	line.split('\t')
	read.append=line[0]
	transcript.append=line[2]
	print(line)
print(read)
print(transcript)
