'''This script takes input file containing 2D points (in each line) as input and produces output file ready to use as input file for snap.svg '''
import sys

'''Take input and output files from command line'''
inputfile=sys.argv[1]
outputfile=sys.argv[2]

with open(inputfile) as f_input:
	content = f_input.readlines()
	content = [x.strip() for x in content]
	lines=len(content)
	f_output = open(outputfile,"w+")
	i = 0
	string = "MLKJIHGFEDCBA"
	word = list(string)
	for x in content:
		if i<lines-1:
			'''Insert words in file'''
			f_output.write(word[i])

		i=i+1
		'''Split each line at comma'''
		import re
		spli=re.split(',', x)
		j=0
		'''insert coordinates in file'''
		for y in spli:
			if j<len(spli)-1 or i==lines-1:
				f_output.write(y+" ")
			else:
				f_output.write(y)
			j=j+1

	f_output.write("Z")
	f_output.close()

f_input.close()
print("Lines read from "+inputfile+"\n"+str(lines))
