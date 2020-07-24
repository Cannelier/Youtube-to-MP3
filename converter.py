import ffmpeg
from pytube import YouTube
import os
import shutil
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-url", help="The URL of the Youtube video. Ex : https://www.youtube.com/watch?v=lvRBv1NSOtQ")
args = parser.parse_args()
#YT_url = "https://www.youtube.com/watch?v=B-IJyNxGLYM"
YT_url = args.url
print(YT_url)
YT_video = YouTube(YT_url)

streams = YT_video.streams.get_audio_only()
streams.download("temp/")

for file in os.listdir("temp/"):
	filenamemp3 = file.replace("mp4","mp3")
	shutil.copyfile("temp/"+file,"output/"+filenamemp3)
	os.remove("temp/"+file)


#streams_mp4 = YT_video.streams.filter(file_extension = "mp4")
