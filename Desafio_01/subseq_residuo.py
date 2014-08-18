# Written by Mathieu Lienard--Mayor, UFRGS, 2014-2

# bases of the DNA sequence
base = [ 'A', 'C', 'T', 'G'];

file = open('Homosapiens_Chromosome7.fasta', 'r');
header = file.readline(); # first line is the header

# reading the first line
seq = file.readline();
# initiating the dictionnary
dico = dict({seq : 1});

# looping through the file
while seq != '':
	if seq != '\n':
		if seq not in dico:
			dico[seq] = 1;
		else:
			dico[seq] = dico[seq]+1;
	# next subsequence
	seq = file.readline(1);
# end while 

print dico;
file.close();

# Written by Mathieu Lienard--Mayor, UFRGS, 2014-2
