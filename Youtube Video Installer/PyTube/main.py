import os
from pytube import YouTube, Playlist, Channel, Search


def main():
    while True:
        url = input("URL: ")
        print("Fetching data...")
        yt = YouTube(url)
        if get_details(yt):
            break
        clear()
    queries = []
    while True:
        choice = input(f"1. Done\n2. Toggle Transcripts\n3. Toggle Video/Sound only\n4. Playlist\nOther: 'q' to Quit; "
                       f"Press enter to Start Over\nYour Choice : ")
        if not choice:
            main()
            return
        if choice == 'q':
            return
        if choice == 1:
            break
        elif choice == 2:
            ...
        elif choice == 3:
            ...
        elif choice == 4:
            ...
        else:
            print("That is not an option!")
        input("Enter to continue...")
        clear()
    # print(get_caption(yt))


def get_details(yt):
    print(f"<{yt.title}> - {yt.author}")
    if input("Is this correct? (Yes/No): ").lower()[0] == "y":
        clear()
        return True
    return False


def get_caption(yt):
    caption = yt.captions.get_by_language_code('en').xml_captions
    return caption.generate_srt_captions()


def clear():
    os.system('cls' if os.name == "nt" else 'clear')


if __name__ == "__main__":
    main()
