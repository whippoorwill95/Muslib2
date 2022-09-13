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
                    # if song != deque(self.songs, 1):
                    if song != self.songs[-1]:
                        file.write(song.path + "\n")
                    else:
                        file.write(song.path)

    def checkArtistNamesOnCaseDiversity(self):
        """doc."""
        for song in self.songs:
            for key in self.artists.keys():
                if song.artist.artistName.lower() == key.lower():
                    if song.artist.artistName != key:
                        print(song.artist.artistName, "!=", key)
                        return "fucked"
        return "seems nothing wrong"

    def addToLibrary(self, source):
        """Add to library."""
        for item in find(source, "*.[mf][pl][3a]*"):
            song = eyed3.load(item)
            self.songs.append(Song(song.tag.title, item, song.tag.album,
                                   self.albums, song.tag.artist, self.artists))

    def aplyTagToSong(self, title, artistName, tagName):
        """Tag to song."""
        # need to add check for versions of songs. I mean should i just transfer albumName to it or?..
        for song in self.songs:
            if title == song.title & song.artist.artistName == artistName:
                song.userTags.add(tagName)

    def aplyTagToAlbum(self, albumName, tagName):
        """Tag to songs of album."""
        for album in self.albums:
            if albumName == album.albumName:
                for song in album.songs:
                    song.userTags.add(tagName)

    def aplyTagToArtist(self, artistName, tagName):
        """Tag to songs by artist."""
        for artist in self.artists:
            if artistName == artist.artistName:
                for song in artist.songs:
                    song.userTags.add(tagName)

    def deleteTagFromSong(self, title, artistName, tagName):
        """Delete tag from song."""
        for song in self.songs:
            if (title == song.title) & (artistName == song.artist.artistName):
                if tagName in song.userTags:
                    song.userTags.remove(tagName)

    def deleteTagFromAlbum(self, albumName, tagName):
        """Delete tag from album."""
        for album in self.albums:
            if albumName == album.albumName:
                for song in album.songs:
                    if tagName in song.userTags:
                        song.userTags.remove(tagName)

    def deleteTagFromArtist(self, artistName, tagName):
        """Delete tag from artist."""
        for artist in self.artists:
            if artistName == artist.artistName:
                for song in artist.songs:
                    if tagName in song.userTags:
                        song.userTags.remove(tagName)

    def hideAuxiliaryArtists():
        """Doc."""
        pass

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
