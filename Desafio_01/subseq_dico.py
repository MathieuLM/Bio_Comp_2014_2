# Written by Mathieu Lienard--Mayor, UFRGS, 2014-2

file = open('Homosapiens_Chromosome7.fasta', 'r');
header = file.readline(); # first line is the header

# reading the first subsequence
seq = file.readline(5);
# initiating the dictionnary
dico = dict({seq : 0});

# looping through the file
while seq != '':
	if seq != '\n':
		if seq not in dico:
			dico[seq] = 0;
	# next subsequence
	seq = file.readline(5);
# end while 

print 'Number of unique subsequences: ' + str(len(dico));

file.close();

# Written by Mathieu Lienard--Mayor, UFRGS, 2014-2
