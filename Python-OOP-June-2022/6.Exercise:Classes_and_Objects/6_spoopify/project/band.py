from project.album import Album


class Band():

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        self.album = album
        for current_album in self.albums:
            if current_album == album:
                return f"Band {self.name} has added their newest album {current_album}."

        return f"Band {self.name} already has {album.name} in their library."

    def remove_album(self, album_name):

        if self.album.published:
            return "Album has been published. It cannot be removed."
        for album in self.albums:
            if album_name not in self.albums:
                return f"Album {album_name} is not found."

        self.albums.remove(album_name)
        return f"Album {album_name} has been removed."

    def details(self):

        new_result = f"Band {self.name}\n"
        for album in self.albums:
            new_result += f"{album.details()}\n"

        return new_result.strip()
