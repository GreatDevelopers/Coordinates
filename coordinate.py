import sys, os

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
                	f_output.write(word[i])
                
		i=i+1
                import re
                spli=re.split(',', x)
                for y in spli:
                    f_output.write(y+" ")
	
	f_output.seek(-1, os.SEEK_END)
	f_output.truncate()
	f_output.write("Z")
