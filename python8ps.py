#!/usr/bin/env python3

import re
#1
#nobody=open('Python_07_nobody.txt','r')#opening file
#poem=nobody.read()#reading contents of file to variable
#for word in re.finditer(r"(Nobody)",poem):#interating through file to find matches for Nobody
#	start=word.start(1)+1#taking start location of each time it found nobody and adding one since position starts at 0
#	end=word.end(1)+1
#	print(start,end)#printing expression for start and end of each nobody

#newpoem=re.sub(r'Nobody','Someone',poem)#substituting nobody for something else
#poemout=open('python8peom.txt','w')#writing new poem to a new file, next several lines
#poemout.write(newpoem)
#print('wrote new poem')


#3
#fastaseq=open('Python_07.fasta','r')
#seqs=fastaseq.read()
#header=re.findall(r'>.+',seqs)#finding all headers for fasta seqs in file and printing
#print(header)
#for thing in re.finditer(r'>(\S+)\W?(.+)',seqs): #iterating through file to find regions that start with >, then capturing until there is a space, then, capturing the rest until the end of the line could also do >(\S+)(.+)
#	ident=thing.group(1)#keeping the first subsetted region, the id
#	desc=thing.group(2)#keepting the second subsetted region, the description
#	print('id:',ident,'desc:',desc)



#4making a fasta parser
fasta={}
fastaseq=open('Python_07.fasta','r')
seqs=fastaseq.read()
for thing in re.finditer(r'>(.+)\n(.+)',seqs):
	header=thing.group(1)
	seq=thing.group(2)
	fasta[header]=seq
print(fasta)

#6
#y is C or T
#r is a or g

fastaseq=open('Python_07_ApoI.fasta','r')
seqs=fastaseq.read()

for restrict in re.finditer(r'(.{3}[AG])(AATT[CT].{2})',seqs):
	print(restrict.group(1)+"^"+restrict.group(2))
	#print(restrict.start(0),restrict.end(0))




