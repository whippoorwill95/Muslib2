"""doc."""


from Album import Album
from Artist import Artist
# import UserTag from UserTag


class Song:
    """doc."""

    def __init__(self, songName, path, albumName, albums, artistName, artists):
        """doc."""
        self.songName = songName
        self.path = path
        self.userTags = set()
        if albumName not in albums.albumName:
            albums.add(Album(albumName))

        if artistName not in artists:
            artists.add(Artist(artistName))

    # SongName = ""
    # Path

    # Album =
    # Reference to an Album object

    # Artist =
    # Reference to an Artist object

    # UserTags = set()
    # Set of Usertags
