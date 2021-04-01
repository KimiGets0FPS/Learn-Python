import pytube


# PATH TO VIDEO
SAVE_PATH = input("Path you want to save on: ")
if not SAVE_PATH:
    SAVE_PATH = "E:/Videos And YT/Download Youtube Videos/Memes"

# OPTIONAL NAME
NAME = input("Name for saving: ")

# LINK FOR VIDEO
LINK = input("Link for video: ")


pytube.YouTube(LINK).streams.get_highest_resolution().download(output_path=SAVE_PATH, filename=NAME)
