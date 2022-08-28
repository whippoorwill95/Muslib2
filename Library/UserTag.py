"""doc."""


# from Album import Album
# from Song import Song


Source = None


class UserTag:
    """doc."""

    def __init__(self, Name=None):
        """Build class."""
        if Name is not None:
            self.TagName = Name
            self.Albums = set()
            self.Songs = set()

    def addTagToAlbum(self, album):
        """Add tag to album."""
        self.Albums.add(album)

    def addTagToSong(self, song):
        """Add tag to song."""
        self.Songs.add(song)
