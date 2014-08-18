# Written by Mathieu Lienard--Mayor, UFRGS, 2014-2

file = open('Homosapiens_Chromosome7.fasta', 'r');
header = file.readline(); # first line is the header

# using a list to store the encountered subsequences
seq_list = [];
# reading the first subsequence
seq = file.readline(5);

# looping through the file
while seq != '':
	if seq != '\n':
		# insert into the list
		seq_list.append(seq);
		# remove previous occurence if it exists
		if seq_list.count(seq) > 1:
			seq_list.remove(seq);
			#print 'Already seen: ' + seq;
		else:
			#print 'New subsequence: ' + seq;
			pass;
	# next subsequence
	seq = file.readline(5);
# end while 

print 'Number of unique subsequences: ' + str(len(seq_list));

file.close();

# Written by Mathieu Lienard--Mayor, UFRGS, 2014-2
