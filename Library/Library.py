"""doc."""


import eyed3
from Library.Song import Song
# from collections import deque
# this shit is broken what deque is?


# It's a plug
from Utils.Search import find


class Library:
    """doc."""

    def __init__(self, source=None):
        """doc. Source should be dir."""
        self.songs = list()
        self.albums = dict()
        self.artists = dict()
        if source is not None:
            for item in find(source, "*.[mf][pl][3a]*"):
                song = eyed3.load(item)
                self.songs.append(Song(song.tag.title, item, song.tag.album,
                               self.albums, song.tag.artist, self.artists))

    def aplyTagToAllLibrary(self, tagName):
        """doc."""
        for song in self.songs:
            song.userTags.add(tagName)

    def makePlaylistFromUserTag(self, tagName):
        """One Tag at start."""
        with open("pl.m3u8", "w", encoding="utf-8") as file:
            file.write("#EXTM3U" + "\n")
            for song in self.songs:
                if tagName in song.userTags:
                    #if song != deque(self.songs, 1):
                    if song != self.songs[-1]:
                        file.write(song.path + "\n")
                    else:
                        file.write(song.path)

        # tagObjects = self.TagObject(Source)
        # foreach tag in tagobjects
        # song = new Song object
        # songs.add(song)
        # tagoobjects SHOULD BE set or list of eyed3.tag objects
        # main object is !Set of songs
        # fill set with songs in Source

    # @property
    # def TagObject(self, path):
    #     """doc."""
    #     try:
    #         eyed3object = eyed3.load(path)
    #         return eyed3object.tag
    #     except eyed3.Error:
    #         print("Error on reading tags")
