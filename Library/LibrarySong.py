"""doc."""


import eyed3


# It's a plug


class LibrarySong:
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
    
    @property
    def TagObject(self, path):
        """doc."""
        try:
            eyed3object = eyed3.load(path)
            return eyed3object.tag
        except eyed3.Error:
            print("Error on reading tags")
