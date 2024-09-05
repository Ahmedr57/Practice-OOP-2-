# Develop a class MusicPlayer that uses composition to include a class Playlist. Implement methods in Playlist to add and remove songs. 
# Then, create a method in MusicPlayer that plays a song using polymorphism to allow different types of songs (like MP3, WAV) to be played using the same method signature.

class Playlist:
    def __init__(self):
        self.song_list= []
        pass

    def add_song(self, song):
        self.song_list.append(song)

    def remove_song(self, song):
        if song in self.song_list:
            self.song_list.remove(song)


class MusicPlayer:
    def __init__(self):
        self.playlist1 = Playlist()

    def add_song_to_playlist(self, song):
        self.playlist1.add_song(song)
        
    def remove_song_from_playlist(self, song):
        self.playlist1.remove_song(song)

    def play_song(self, song):
        if song.endswith('.mp3'):
            if song in self.playlist1.song_list:
                print(f"Playing MP3 song: {song}")
            else:
                print(f"{song} not present in Playlist!")
        elif song.endswith('.wav'):
            if song in self.playlist1.song_list:
                print(f"Playing WAV song: {song}")
            else:
                print(f"{song} not present in Playlist!")


player = MusicPlayer()

player.add_song_to_playlist("Song1.mp3")
player.add_song_to_playlist("Song2.wav")
player.add_song_to_playlist("Song3.mp4")
player.add_song_to_playlist("Song4.wav")

player.play_song("Song1.mp3")
player.remove_song_from_playlist("Song2.wav")
player.play_song("Song2.wav")
player.play_song("Song4.wav")