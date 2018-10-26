#!/usr/bin/env python3
import re
#import sys

#fastafile=sys.argv[1]
fastafile=open('probs8test.fasta','r')
seqs={}
for line in fastafile:
	header=re.search(r'^>(.+)',line)
	value=''
	if header:
		name=header.group(1)
		seqs[name]=()
	else:
		value+=line
		seqs[name]=value
		
print(seqs)



 
