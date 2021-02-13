from pytube import YouTube

# Warning
print("If no print 'Download Success', then there is a problem.")

# PATH TO VIDEO
SAVE_PATH = "E:/Download Youtube Videos"

# OPTIONAL NAME
NAME = ""

# LINK FOR VIDEO
link = "https://www.youtube.com/watch?v=UKAr7FsTNgY"

YouTube(link).streams.first().download(output_path=SAVE_PATH, filename=NAME)
print("Download Success.")
