import sys, argparse

# Coded by Suleiman Alothman @sulealothman
# Basic Converter from rgb to hex or reverse
# 2019/3/24



# Check is hex value or else, not used in this example
def check_IsHex(hexString):
	try:
		int(hexString,16)
		return True
	except ValueError:
		return False

# Check is rgb value or else, not used in this example
def check_IsRGB(rgbString):
	for int(x) in rgbString.split(','):
		if x < 0 or x > 255:
			return False
	return True

# Convert from RGB Value to HEX Value method
def Rgb2Hex(rgb):
	return '#%02x%02x%02x' % tuple(int(x.strip()) for x in rgb.split(','))

# Convert from HEX Value to RGB Value method
def Hex2Rgb(hexColor):
	return tuple(int(hexColor[i:i+2], 16) for i in (0, 2 ,4))


# Added arguments for used with command line
parser = argparse.ArgumentParser(description="Convert RGB & HEX example")
parser.add_argument('-x','--r2h',type=str,help='RGB to Hex')
parser.add_argument('-r','--h2r',type=str,help='Hex to RGB')
args = parser.parse_args()

if __name__ == "__main__":
	#Check if use any arguments or else and begin program
	if(args.r2h != None):
		try:
			rgbColor = Rgb2Hex(args.r2h)
			print("RGB Color :",args.r2h)
			print("Hex Color :",rgbColor)
		except:
			print("Err: incurrept converting")
	elif(args.h2r != None):
		try:
			hexColor = Hex2Rgb(args.h2r.lstrip("#"))
			print("Hex Color :",args.h2r)
			print("RGB Color :",hexColor)
		except:
			print("Err: incurrept converting")
	else:
		print("RGB to HEX : 1 \r\nHEX to RGB : 2")
		SelectOption = input("Please Select Function : ")
		if(int(SelectOption) == 1):
			inputRGB = input("Enter RGB Color : ")
			try:
				print("Hex Color :",Rgb2Hex(inputRGB))
			except:
				print("Err: incurrept converting")
		elif(int(SelectOption) == 2):
			inputHex = input("Enter HEX Color : ")
			try:
				print("RGB Color :",Hex2Rgb(inputHex.lstrip("#")))
			except:
				print("Err: incurrept converting")
		else:
			print("Your don't selected any option")
	sys.exit()

