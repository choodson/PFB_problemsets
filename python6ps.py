#!/usr/bin/env python3


#1+2
#python6=open('Python_06.txt', 'r')
#python6out=open('upperpython6.txt','w')
#for line in python6:
#	line=line.rstrip()
#	up=line.upper()
#	python6out.write(up+'\n')
#print('python6out.txt written')

#3

#python6seq=open('Python_06.seq.txt', 'r')
#python6seq=open('python6test.txt', 'r')

#for line in python6seq:
#	line=line.rstrip()
#	ident, seq0=line.split()
#	seq=seq0[::-1]
#	seq1=seq.replace('T','a')
#	seq2=seq1.replace('A','t')
#	seq3=seq2.replace('G','c')
#	seq4=seq3.replace('C','g')
#	seq5=seq4.upper()
#	print('>',ident,'reverse complement', '\n',seq5)	

#4
python6fasta=open('Python_06.fastq', 'r')
linenum=0
count=0
counter=0
length=0
for line in python6fasta:
	line=line.rstrip()
	count+=len(line)
	linenum+=1
	length+=len(line)
	counter+=1
ave=length/counter
print('number of lines',linenum)
print('total characters',count)
print('average line length',ave)

	



