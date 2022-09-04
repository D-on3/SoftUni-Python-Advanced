from project.song import Song


class Album():

    def __init__(self, name, *args):
        self.name = name
        self.published = False
        self.songs = [*args]

    def add_song(self, song: Song):

        if song.single:
            return f"Cannot add {self.name}. It's a single"
        if self.published:
            return "Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_songs(self, song_name):
        if self.published:
            return "Cannot remove songs. Album is published."

        for song in self.songs:
            if song == song_name:
                self.songs.remove(song)
                return f"Removed song {song_name} from album {self.name}."
        return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = f"Album {self.name}\n"
        for song in self.songs:
            result += f"== {song.name}\n"

        return result.strip()


