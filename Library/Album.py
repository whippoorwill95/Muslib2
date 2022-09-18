"""doc."""


from Library.Artist import Artist
from Library.Song import Song


class Album:
    """doc."""

    def __init__(self, song: Song, artist: Artist, name: str):
        """doc."""
        self.albumName = name
        self.songs = {song}
        self.artist = artist

    def addSong(self, song: Song) -> None:
        """doc."""
        self.songs.add(song)
