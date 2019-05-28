


import sys


# python3 cipher.py [StringToConvert] [spaces to shift]
# distance from lowercase is 7

stringInput = sys.argv[1]
spacesToShift = sys.argv[2]


def printStringInput(stringArgument):
	for i in sys.argv[1]:
		print(ord(i))

def shiftOver(stringargument, spacesToShiftInput):
	output = ""
	for i in stringargument:
		# Capitals going above

		if(65<=ord(i)<=90):
			if(ord(i)+spacesToShiftInput>90):
				diff = 90 - ord(i)
				newval = diff + 65
				output = output + chr(newval)
			else:
				output = output + chr((ord(i)+spacesToShiftInput))

		# Lowercase going above
		elif(97<=ord(i)<=122):
			if(ord(i)+spacesToShiftInput>122):
				diff = 122 - ord(i)
				newval = diff + 97
				output = output + chr(newval)
			else:
				output = output + chr((ord(i)+spacesToShiftInput))
	return output
	
	

def main():
	print(stringInput)
	print(shiftOver(stringInput, int(spacesToShift)))

if __name__ == "__main__":
	main();