import sys, argparse
import youtube_dl

# Coded by Suleiman Alothman @sulealothman
# https://twitter.com/SuleAlOthman/status/1015482549798359042
parser = argparse.ArgumentParser(
	description="Script name : Download-Youtube, Ver. : 0.1, Author : SuleAlOthman",
	usage=""" Example #1 : python3 download-youtube.py -l https://www.youtube.com/watch?v=XXXXXXXXXXX \r\n
	Example #2 : python3 download-youtube.py -f links.txt \r\n
	Example #3 : python3 download-youtube.py -f links.txt -e mp4 \r\n""")
parser.add_argument('-f', '--file',type=str,help='Text file for links')
parser.add_argument('-l', '--link',type=str,help='Video Url')
parser.add_argument('-e', '--extension',nargs='?',default="mp3",type=str,help='extension file : mp3 or mp4')
args = parser.parse_args()

def youtubeDownload(url,ext="mp3"):
	if ext == "mp3":
		ydl_opts = {
			'format': 'bestaudio/best',
			'postprocessors': [{
				'key' : 'FFmpegExtractAudio',
				'preferredcodec': 'mp3',
				'preferredquality': '192',
				}],
		}
	else:
		ydl_opts = {
			'format' : 'bestvideo',
			'postprocessors' : [{
				'key' : 'FFmpegVideoConvertor',
				'preferedformat' : 'mp4',
				}]
		}

	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download([url])


if __name__ == "__main__":

	if(args.file != None):
		path = args.file
		try:
			linksFile = open(path, "r")
			for link in linksFile:
				try:
					youtubeDownload(link, args.extension.strip())
				except:
					print(link + " : is incorrupt")
		except:
			print("Not found the file")
		print("\r\n- #   Finished downloading ..")
		sys.exit()
	elif(args.link != None):
		url = args.link
		try:
			youtubeDownload(url, args.extension.strip())
		except:
			print(url + " incurrept link")
	else:
		url = input("Enter youtube url : ")
		try:
			youtubeDownload(url, args.extension.strip())
		except:
			print(url + "incurrept link")



print("\r\n- #   Finished downloading ..")