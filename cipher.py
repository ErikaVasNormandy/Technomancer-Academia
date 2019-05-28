import sys


# python3 cipher.py [StringToConvert] [spaces to shift]
spacesToShift = sys.argv[2]

def shiftOver(stringargument):
	output = ""
	for i in stringargument:
		# Capitals going above

		if(65<=ord(i)<=90):
			if(ord(i)+4>90):
				diff = 90 - ord(i)
				newval = diff + 65
				output = output + chr(newval)
			else:
				output = output + chr((ord(i)+4))

		# Lowercase going above
		elif(97<=ord(i)<=122):
			if(ord(i)+4>122):
				diff = 122 - ord(i)
				newval = diff + 97
				output = output + chr(newval)
			else:
				output = output + chr((ord(i)+4))
	return output
	
	

def main():
	print(sys.argv[1])
	# distance from lowercase is 7
	
	#for i in sys.argv[1]:
	#	print(ord(i))
	print(shiftOver(sys.argv[1]))

if __name__ == "__main__":
	main();