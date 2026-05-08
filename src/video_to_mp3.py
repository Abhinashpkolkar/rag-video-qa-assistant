# Converts the videos to mp3 
import os 
import subprocess

files = os.listdir("videos") 
for file in files: 
    tutorial_number = file.split(" [")[0].split(" #")[1]  #This line splits the file name and stores them in a list and then uses it to get the tutorial number.
    file_name = file.split(" ｜ ")[0] # Similarly for file name.
    print( tutorial_number,  file_name)
    subprocess.run(["ffmpeg", "-i", f"videos/{file}", f"audios/{tutorial_number}_{file_name}.mp3"])
