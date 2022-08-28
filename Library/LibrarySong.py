"""doc."""


from LibraryAbstractBaseClass import LibraryABC


# It's a plug


class LibrarySong(LibraryABC):
    """doc."""

    def __init__(self, Source=None):
        """doc. Source should be dir."""
        # tagObjects = self.TagObject(Source)
        # foreach tag in tagobjects
        # song = new Song object
        # songs.add(song)
        # tagoobjects SHOULD BE set or list of eyed3.tag objects
        # main object is !Set of songs
        self.songs = set()
        # fill set with songs in Source
