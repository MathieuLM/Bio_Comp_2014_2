# Written by Mathieu Lienard--Mayor, UFRGS, 2014-2

file = open('Homosapiens_Chromosome7.fasta', 'r');
header = file.readline(); # first line is the header

X = "TTT"; # marker of separation between sequences

# reading the first line
line = file.readline().strip();
# initializing the dictionnary with a fake key
dico = dict({'fake' : 0 });

# looping through the lines
#for i in xrange(3):
while line != '':
	# using the marker to split the line
	#print line+'\n\n\n';
	seq = line.split(X);
	#print seq;
	size = len(seq);
	# insert the subsequences detected
	#for i in xrange(0, size-1):
		#if seq[i] not in dico:
			#dico[seq[i]] = 0;
	# concatening the leftover with the next line
	leftover = seq[size-1];
	#print leftover;
	line = file.readline().strip();
	#print line;
	line = leftover + line;

print 'Number of unique subsequences: ' + str(len(dico));

file.close();

# Written by Mathieu Lienard--Mayor, UFRGS, 2014-2
