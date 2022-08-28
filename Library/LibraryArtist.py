"""doc."""


from LibraryAbstractBaseClass import LibraryABC


Source = None
# It's a plug


class LibraryArtist(LibraryABC):
    """doc."""

    def __init__(self, Source=None):
        """doc."""
        # main object is !Set of artist
        self.artists = set()
        # fill set with artists in Source
