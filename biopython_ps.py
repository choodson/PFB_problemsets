#!/usr/bin/env python3

from Bio import SeqIO
fasta_file="Python_08.fasta"
seq_big=0
seq_small=100000000
gc_total=[]
seq_num=0
nt_num=0
def gc_cont(sequence):
	G_count=sequence.count("G")
	C_count=sequence.count("C")
	length_sequence=len(sequence)
	gc=(G_count+C_count)/length_sequence
	return gc

for seq_record in SeqIO.parse(fasta_file,"fasta"):
	print('ID',seq_record.id)
	print('Sequence',seq_record.seq)
	print('Description',seq_record.description)
	if len(seq_record)>seq_big:
		seq_big=len(seq_record)
		longest_id=seq_record.id
	if len(seq_record)<seq_small:
		seq_small=len(seq_record)
		shortest_id=seq_record.id
	gc_total.append(gc_cont(seq_record.seq))
	seq_num+=1
	nt_num+=len(seq_record.seq)

average_gc=sum(gc_total)/len(gc_total)
print('the total number of nt is:',nt_num)
print('the total number of sequences is:', seq_num)
print('the average gc_content is:', average_gc)
print('the highest gc content is:',max(gc_total))	
print('the lowest gc content is:',min(gc_total))	
print('the longest seq is:',seq_big, longest_id)	
print('the shortest seq is:',seq_small,shortest_id)	
