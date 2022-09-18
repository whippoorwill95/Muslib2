"""doc."""

# from Library.Album import Album
# from Library.Song import Song


from Library.Album import Album
from Library.Song import Song


class Artist:
    """doc."""

    def __init__(self, song: Song, name: str):
        """doc."""
        self.albums = set()
        self.songs = {song}
        self.artistName = name

    def addSong(self, song: Song) -> None:
        """doc."""
        self.songs.add(song)

    def addAlbum(self, album: Album) -> None:
        """doc."""
        self.albums.add(album)
