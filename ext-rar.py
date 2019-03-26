import sys, argparse, rarfile

# Script : Extract rar files
# Ver. : 0.1 Alpha
# Requirement : install unrar by brew for macos | by apt for linux | download unrar for internet
# How to use? python3 erar.py -rf "path/filename.rar" -el
# Author : Suleiman Al-Othman




parser = argparse.ArgumentParser(description="Script for extract rar files, Version 0.1 alpha")

parser.add_argument('-rf','--rarfile',type=str,help='Select rar File')
parser.add_argument('-el','--extractall',help='Extract All Files', action="store_true")
parser.add_argument('-p','--password',type=str,help='Password rar')
parser.add_argument('-i','--info',help='Info list for rar file',action="store_true")
parser.add_argument('-f','--onefile',type=str,help='Extract one file')
parser.add_argument('-d','--directory',type=str,help='Directory Name to Extract')
args = parser.parse_args()

if __name__ == "__main__":

	if(args.rarfile != None):
		rarFile = rarfile.RarFile(args.rarfile)

		if(rarFile.needs_password()):
			if(args.password != None):
				passRAR = args.password
			else:
				passRAR = input('Please Enter RAR Password : ')

		if(args.extractall):
			rarFile.extractall(path=args.directory if args.directory != None else None,
				members=None,
				pwd=passRAR if args.password != None else None)
		elif(args.onefile):
			rarFile.extract(member=args.onefile,path=args.directory if args.directory != None else None,
				pwd=passRAR if args.password != None else None)
		elif(args.info):
			for i in rarFile.infolist():
				print(i.filename)
		else:
			print("value")
	else:
		rarInput = input("Enter rar path :")
		rarFile = rarfile.RarFile(rarInput)
		if(rarFile.needs_password()):
			passRAR = input("Enter rar password : ")
		else:
			passRAR = None


		selectDir = input("Enter directory for extract : ")
		if(selectDir.strip() == ""):
			selectDir = None
		print("Extract All - 1")
		print("Extract one file - 2")
		print("Print All info list - 3")


		SelectOption = input("Enter select option : ")

		if(int(SelectOption) == 1):
			rarFile.extractall(path=selectDir,members=None,pwd=passRAR)
		elif(int(SelectOption) == 2):
			memberInput = input("Enter file name you want extract : ")
			rarFile.extract(member=memberInput,path=selectDir,pwd=passRAR)
		elif(int(SelectOption) == 3):
			for i in rarFile.infolist():
				print(i.filename)
		else:
			print("value")
