"""doc."""

# I use TYPE_CHECCKING to work with type hints without getting circular import error
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .Song import Song
    from .Artist import Artist


class Album:
    """doc."""

    def __init__(self, song: 'Song', artist: 'Artist', name: str):
        """doc."""
        self.albumName = name
        self.songs = {song}
        self.artist = artist

    def addSong(self, song: 'Song') -> None:
        """doc."""
        self.songs.add(song)
