#!/usr/bin/env python3

sequence1='AGTCTGTCA'
sequence2='GATCTCTGC'


def score(seq1,seq2):
	score=0
	length_seq=len(seq1)	
	for nt in range(0,length_seq):
		if seq1[nt]==seq2[nt]:
			score+=1
		else:
			score-=1
	return score
def nt_comp(seq):
	for nt in seq:
		seq=seq[::-1]
		seq1=seq.replace('T','a')
		seq2=seq1.replace('A','t')
		seq3=seq2.replace('G','c')
		seq4=seq3.replace('C','g')
		seq5=seq4.upper()
		return seq5
rc_sequence1=nt_comp(sequence1)
rc_sequence2=nt_comp(sequence2)

print(score(sequence1,sequence2))
print(score(rc_sequence1,sequence2))
print(score(sequence1,rc_sequence2))
print(score(rc_sequence1,rc_sequence2))




#print(rc_sequence1)
#print('>',ident,'reverse complement', '\n',seq5)
