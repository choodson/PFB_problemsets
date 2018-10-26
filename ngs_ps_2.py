#!/usr/bin/env python3




fastq_file = open('four_reads.fastq',"r")
counter=0
for line in fastq_file:
	counter+=1
	if counter%2==0:	
		line.rstrip()
		linelength=len(line)-4
		newline=line[0,linelength]
		print(linelength)
