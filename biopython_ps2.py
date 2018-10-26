#!/usr/bin/env python3
import re
from Bio import SeqIO
#fasta_file="uniprot_sprot.fasta"
fasta_file="Python_07.fasta"
seq_ids=[]

for seq_record in SeqIO.parse(fasta_file,"fasta"):
	if seq_record
	header=re.search(r'^>(\S+)(.+)',seq_record)
	seq_ids.append(header.group(1))

