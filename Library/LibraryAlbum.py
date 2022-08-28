"""doc."""


# from Song import Song
from LibraryAbstractBaseClass import LibraryABC

Source = None
# It's a plug


class LibraryAlbum(LibraryABC):
    """doc."""

    def __init__(self, Source):
        """doc."""
        # tagObject = self.TagObject(Source)
        # main object is !Set of albums
        self.albums = set()
        # fill set with albums in Source
