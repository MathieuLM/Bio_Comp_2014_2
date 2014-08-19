# Written by Mathieu Lienard--Mayor, UFRGS, 2014-2

file = open('Homosapiens_Chromosome7.fasta', 'r');
header = file.readline(); # first line is the header

# number of subsequences encountered
nb_seq = 0;
#number of consecutive T read
nb_T = 0;

# reading the rest of the file
line = file.read().strip();
size = len(line);
# going through the file
for i in range(size):
    if line[i] == 'T':
        nb_T = nb_T + 1;
        if nb_T == 3:
            nb_T = 0;
            nb_seq = nb_seq + 1;
            
print('Number of unique subsequences: ' + str(nb_seq+1));

file.close();

# Written by Mathieu Lienard--Mayor, UFRGS, 2014-2
