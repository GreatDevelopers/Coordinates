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
	for x in content:
		'''Insert words in file'''
		if i==0:
			f_output.write("M")
		elif i==1:
			f_output.write("L")

		i=i+1
		'''Split each line at comma'''
		import re
		spli=re.split(',', x)
		'''insert coordinates in file'''
		j=0
		for y in spli:
			if i==1 and j==len(spli)-1:
				f_output.write(y)
			elif i==lines and j==len(spli)-1:
				f_output.write(y)
			else:
				f_output.write(y+" ")

			j=j+1

	f_output.write("Z")
	f_output.close()

f_input.close()
print("Lines read from "+inputfile+"\n"+str(lines))
