#!/usr/bin/env python3
#import sys

# we must define our functions above the main script code:

    

#fasta_fileobj = open(pfb2018/input_files/human_cds.fasta, 'r')
fasta_fileobj = open('Python_07.fasta', 'r')

# copy sys.stdout's file object to a new variable to use
# to write to. This enables our script to write to stdout
# by default, but allows the variable to be redefined to
# a new file object if we wish to write to a file directly:
#output_fileobj = sys.stdout
#if len(sys.argv) == 3:  # user gave an output file name:
#	output_fileobj = open(sys.argv[2], 'w')
def nt_freq(seq):
	A_freq=seq.count('A')/len(seq)
	T_freq=seq.count('T')/len(seq)
	G_freq=seq.count('G')/len(seq)
	C_freq=seq.count('C')/len(seq)
	return "A",A_freq,"T",T_freq,"G",G_freq,"C",C_freq
sequence_name = ''
sequence_desc = ''
sequence_string = ''
human_cds={sequence_name:sequence_desc}
for line in fasta_fileobj:  # pull a line out from the file
	line = line.rstrip()
	if line.startswith('>'):
		if len(sequence_string) > 0:
            # do something interesting with the stored info				
			human_cds={sequence_name:sequence_string}
			NT_count=nt_count(sequence_string)
# Now output the processed sequence to a file:
		#output_fileobj.write(">{} {}\n{}\n".format(sequence_name, sequence_desc, rc_sequence))
			sequence_string = ''  # reset for the new sequence
		line = line.lstrip('>')
		sequence_info = line.split(maxsplit=1)  # split on only first space
		sequence_name = sequence_info[0]
		if len(sequence_info) > 1:
			sequence_desc = sequence_info[1]
		else:
			sequence_desc = ''
	else:
		sequence_string += line  # incrementally elongate seq

if len(sequence_string) > 0:
	NT_count=nt_count(sequence_string)

    #output_fileobj.write(">{} {}\n{}\n".format(
     #   sequence_name, sequence_desc, rc_sequence))


print(human_cds)
print(NT_count)

# Make sure to close your output files or risk losing data!    
#output_fileobj.close()
