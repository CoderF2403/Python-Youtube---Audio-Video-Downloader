import pafy
from pytube import YouTube
import sys


SAVE_PATH = '/home/faisal/Downloads'


def audiodownload(url):
    try:
        video = pafy.new(url)
        bestaudio = video.getbestaudio()
        print(f'Downloading {video.title}!!')
        bestaudio.download(SAVE_PATH)
        print('Downloaded !')
        start()
    except Exception:
        print('SOME ERROR OCCURRED ! PLEASE RESTART AGAIN !')


def videodownload(url):
    try:
        yt = YouTube(url)
        print(f'Downloading {yt.title}')
        video = yt.streams.get_highest_resolution()
        video.download(SAVE_PATH)
        print('Downloaded !')
        start()
    except Exception:
        print('SOME ERROR OCCURRED ! PLEASE RESTART AGAIN !')


def start():
    try:
        print('WELCOME TO DOWNLOADER\n'
              'You can now download youtube videos and audios.\n'
              'Press E to exit.')
        choice = input('1) Audio   2) Video\nPlease Enter Your Choice : ')
        if choice == '1':
            url = input('Enter url : ')
            audiodownload(url)
        elif choice == '2':
            url = input('Enter url : ')
            videodownload(url)
        elif choice == 'E' or choice == 'e':
            print('PROGRAM CLOSED !!')
            sys.exit()
        else:
            print('Please Enter Again - Unidentified Choice.')
            start()
    except Exception:
        print('SOME ERROR OCCURRED ! PLEASE TRY AGAIN !')
        start()

if __name__ == '__main__':
    start()
