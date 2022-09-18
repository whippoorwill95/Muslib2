"""doc."""


from Library.Album import Album
from Library.Artist import Artist


class Song:
    """doc."""

    def __init__(self, title: str, path: str, albumName: str, albums: dict, artistName: str, artists: dict):
        """doc."""
        self.title = title
        self.path = path
        self.userTags = set()
        # проверяем есть ли артист в библиотеке если нет создаём, если есть ссылаемся на него
        if artistName not in artists.keys():
            self.artist = Artist(self, artistName)
            artists[artistName] = self.artist
        else:
            self.artist = artists[artistName]

        # то же самое с альбомом но еще добавляем к артисту альбом если нужно
        if (albumName, artistName) not in albums.keys():
            self.album = Album(self, self.artist, albumName)
            self.artist.addAlbum(self.album)
            albums[(albumName, artistName)] = self.album
        else:
            self.album = albums[(albumName, artistName)]
        self.album.addSong(self)
        self.artist.addSong(self)
