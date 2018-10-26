import os
import sys
import jsbeautifier

# usage: python js-extractor.py <file>

	
def splitFile(inputFile):
	f=open(inputFile)

	# reads the file
	file=f.read()

	# splits the file of multiple scripts into seperate strings
	splitFiles = file[8:].split("\nhttps://")

	# checks to see if the directory is present
	for i in range(len(splitFiles)):
		directory = '/'.join(filter(None,splitFiles[i].split()[0].split("/"))[:-1])
		fileName = filter(None,splitFiles[i].split()[0].split("/"))[-1:][0].split('?')[0].split('#')[0]
		fileContents = jsbeautifier.beautify(splitFiles[i][len(splitFiles[i].split()[0]):])
		if os.path.isdir(directory):
			print("Directory Exists: %s " % directory)
		else:
			try:
				os.makedirs(directory)
			except OSError:
				print("Failed %s " % directory)
			else:
				print("Directory Created: %s " % directory)
				
		try:
			if "." not in fileName:
				fileNew = open("%s/%s.js" % (directory, fileName),"w+")
			else:
				fileNew = open("%s/%s" % (directory, fileName),"w+")
		except IOError:
			print('wtf')
			
		fileNew.write(fileContents)
		fileNew.close()
		print("File: %s created." % fileName)
					
		
try:
	inputFile=sys.argv[1]
	splitFile(inputFile)
except IndexError:
	print('usage: python js-extractor.py <file>')
	