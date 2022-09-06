"""doc."""


import eyed3
from Library.Song import Song


# It's a plug
from Utils.Search import find


class Library:
    """doc."""

    def __init__(self, source=None):
        """doc. Source should be dir."""
        self.songs = set()
        self.albums = dict()
        self.artists = dict()
        if source is not None:
            for item in find(source, "*.[mf][pl][3a]*"):
                song = eyed3.load(item)
                self.songs.add(Song(song.tag.title, item, song.tag.album,
                               self.albums, song.tag.artist, self.artists))

        # tagObjects = self.TagObject(Source)
        # foreach tag in tagobjects
        # song = new Song object
        # songs.add(song)
        # tagoobjects SHOULD BE set or list of eyed3.tag objects
        # main object is !Set of songs
        # fill set with songs in Source

    @property
    def TagObject(self, path):
        """doc."""
        try:
            eyed3object = eyed3.load(path)
            return eyed3object.tag
        except eyed3.Error:
            print("Error on reading tags")
