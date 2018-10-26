#!/usr/bin/env python3

from Bio import SeqIO
#fasta_file="Python_07.fasta"
fasta_file="ecoliPB-filtered_0.50.contigs.fasta"
#id_dict=SeqIO.to_dict(
seq_big=0
seq_small=10000000
for seq_record in SeqIO.parse(fasta_file,"fasta"):
	num_contigs=(len(seq_record.id))
	if len(seq_record)>seq_big:
		seq_big=len(seq_record)
		longest_id=seq_record.id

	if len(seq_record)<seq_small:
		seq_small=len(seq_record)
		shortest_id=seq_record.id

print('number of contigs:',num_contigs)
print('the longest contig is:',longest_id,':',seq_length,'bp')
print('the shortest contig is:',shortest_id,':',seq_small,'bp')
