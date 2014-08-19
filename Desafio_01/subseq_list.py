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
		# insert if first occurence
		if seq_list.count(seq) == 0:
			seq_list.append(seq);
	# next subsequence
	seq = file.readline(5);
# end while 

print('Number of unique subsequences: ' + str(len(seq_list)));

file.close();

# Written by Mathieu Lienard--Mayor, UFRGS, 2014-2
