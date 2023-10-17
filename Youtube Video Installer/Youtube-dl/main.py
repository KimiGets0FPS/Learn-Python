from youtube_dl import YoutubeDL

audio_downloader = YoutubeDL({'format': 'bestaudio'})

while True:
    url = input('Enter youtube url: ')
    if url:
        audio_downloader.extract_info(url)
