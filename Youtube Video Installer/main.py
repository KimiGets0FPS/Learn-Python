import pytube


# PATH TO VIDEO
SAVE_PATH = ""

# OPTIONAL NAME
NAME = ""

# LINK FOR VIDEO
LINK = ""


pytube.YouTube(LINK).streams.get_highest_resolution().download(output_path=SAVE_PATH, filename=NAME)
