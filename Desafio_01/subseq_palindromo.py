# Written by Mathieu Lienard--Mayor, UFRGS, 2014-2

file = open('Homosapiens_Chromosome7.fasta', 'r');
header = file.readline(); # first line is the header

# reading the first subsequence
seq = file.readline(7);
# initiating the dictionnary with a fake key
dico = dict({'fake' : 0});

# looping through the file
while seq != '':
	if seq != '\n':
			if seq not in dico:
				rev = seq[::-1];
				if seq == rev:
					dico[seq] = 0;
	# next subsequence
	seq = file.readline(7);
# end while 

del dico['fake'];
print 'Number of unique palindroms: ' + str(len(dico));
print dico;

file.close();

# Written by Mathieu Lienard--Mayor, UFRGS, 2014-2
