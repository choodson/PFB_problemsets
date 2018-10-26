#!/usr/bin/env python3

class DNAseq(object):
	def __init__(self, sequence, sequence_name, organism):
		self.sequence=sequence
		self.sequence_name=sequence_name
		self.organism=organism
	def sequence_length(self):
		length=len(self.sequence)
		return length
	def nt_comp(self):
		a_count=self.sequence.count('A')
		t_count=self.sequence.count('T')
		g_count=self.sequence.count('G')
		c_count=self.sequence.count('C')
		#comp=[a_count,t_count,g_count,c_count]
		return 'A:', a_count, 'T:', t_count, 'G:',g_count,'C:',c_count 
	def gc_content(self):
		g_count=self.sequence.count('G')
		c_count=self.sequence.count('C')	
		length=len(self.sequence)
		gc_cont=((g_count+c_count)/length)*100
		return gc_cont
	def fasta_format(self):
		fasta=''>',self.sequence_name,'\n',self.sequence'
		return fasta


dna_obj_1=DNAseq('TATATGCGCGTCGCTAGAGATCGCG','seq1','Liposcelis bostrychophila')
print(dna_obj_1.sequence)
print(dna_obj_1.sequence_name)
print(dna_obj_1.organism)
print(dna_obj_1.sequence_length())
print(dna_obj_1.nt_comp())
print(dna_obj_1.gc_content())
print(dna_obj_1.fasta_format())
