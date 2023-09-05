from sclib import SoundcloudAPI, Track
import os

def download_song(track):
    filename = f'./{track.artist} - {track.title}.mp3'

    with open(filename, 'wb+') as file:
        track.write_mp3_to(file)

    print(f'File saved: {filename}')

def download_songs_from_file(file_path):
    with open(file_path, 'r') as file:
        urls = file.readlines()
        for url in urls:
            url = url.strip()
            track = api.resolve(url)
            assert type(track) is Track
            download_song(track)
    
    print("All songs downloaded and saved'")

if __name__ == "__main__":
    api = SoundcloudAPI()
    
    print("Welcome to SoundCloud Downloader! - Author: Ryan Horner")
    print("If you'd like to download a single song, enter 1. \nIf you'd like to download multiple songs, enter 2 and provide a songs.txt file.")
    num_songs = int(input("Enter the number of songs you'd like to download: "))
    if num_songs == 1:
        song_url = input('Enter a SoundCloud URL: ')
        track = api.resolve(song_url)
        assert type(track) is Track
        download_song(track)
    elif num_songs > 1:
        download_songs_from_file('songs.txt')
    else:
        print("Invalid number of songs.")
