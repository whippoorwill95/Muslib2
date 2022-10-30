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
        #_as = set()
        #_ss = set()
        self.albums = set()
        self.songs = set()
        self.artistName = name

    def __repr__(self) -> str:
        """doc."""
        return f"""
    (
    Имя артиста: {self.artistName}
    Связанные альбомы: {self.albums}
    Связанные песни: {self.songs}
    )
    """

    def addSong(self, song: 'Song') -> None:
        """doc."""
        self.songs.add(song)

    def addAlbum(self, album: 'Album') -> None:
        """doc."""
        self.albums.add(album)
