import pytube


# PATH TO VIDEO
SAVE_PATH = "E:/Download Youtube Videos"

# OPTIONAL NAME
NAME = "My Man throws computer into trash"

# LINK FOR VIDEO
LINK = "https://www.youtube.com/watch?v=7jvWb-rHipo"


pytube.YouTube(LINK).streams.get_highest_resolution().download(output_path=SAVE_PATH, filename=NAME)
