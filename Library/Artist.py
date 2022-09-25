"""doc."""

# I use TYPE_CHECCKING to work with type hints without getting circular import error
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .Song import Song
    from .Album import Album


class Artist:
    """doc."""

    def __init__(self, song: 'Song', name: str):
        """doc."""
        self.albums = set()
        self.songs = {song}
        self.artistName = name

    def addSong(self, song: 'Song') -> None:
        """doc."""
        self.songs.add(song)

    def addAlbum(self, album: 'Album') -> None:
        """doc."""
        self.albums.add(album)
