import os
for file in os.listdir("D:\music"):
    if file.endswith(".mp3"):
        print(os.path.join("D:\music"),file)