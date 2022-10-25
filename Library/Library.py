"""doc."""


from typing import Set
from mutagen.id3 import ID3
# from mutagen.id3 import ID3NoHeaderError
from Library.Artist import Artist
from Library.Album import Album
from Library.Song import Song
import os
import re
# from collections import deque
# this shit is broken what deque is?

import logging
import logging.config
from logs.settings import logger_config
logging.config.dictConfig(logger_config)
logger = logging.getLogger('app_logger')


class Library:
    """doc."""

    def __init__(self, regexPattern=None, source=None, ):
        """doc. Source should be dir.

        dictionary "__artists" has string key (artistName) and value of Atist object
        dictionary "__albums" has two string keys (albumName, artistName) and value of Album object
        these dictionaries are filled in the Song constructor. I did that since object of class Song has property-refference to Artist and Album objects
        """
        Albums = dict[tuple[str, str], Album]
        Artists = dict[str, Artist]
        Songs = list[Song]
        self.__songs = Songs()
        self.__albums = Albums()
        self.__artists = Artists()
        if (source is not None) and (regexPattern is not None):
            _templist = list()
            # I want to make temporary list of full file pathes which is destroyed after library is stuffed. But i'm not sure if i do right
            for address, dirs, files in os.walk(source):
                for name in files:
                    _templist.append(f"{os.path.join(address, name)}")

            # Calling constructor of class Song which cause constructors of Album & Artist classes.
            for item in _templist:
                try:
                    if re.search(regexPattern, item):
                        song = ID3(item)
                        self.__songs.append(Song(song["TIT2"].text[0], item, song["TALB"].text[0],
                                          self.__albums, song['TPE1'].text[0], self.__artists))
                except:
                    # logger.exception(f'item = {item}')
                    pass

    def aplyTagToAllLibrary(self, tagName: str) -> None:
        """doc."""
        for song in self.__songs:
            song.userTags.add(tagName)

    def makePlaylistFromUserTag(self, tagName: str) -> None:
        """Need to complete."""
        with open("pl.m3u8", "w", encoding="utf-8") as file:
            file.write("#EXTM3U" + "\n")
            for song in self.__songs:
                if tagName in song.userTags:
                    # if song != deque(self.__songs, 1):
                    if song != self.__songs[-1]:
                        file.write(song.path + "\n")
                    else:
                        file.write(song.path)

    def checkArtistNamesOnCaseDiversity(self) -> str:
        """Need to complete."""
        for song in self.__songs:
            for key in self.__artists.keys():
                if song.artist.artistName.lower() == key.lower():
                    if song.artist.artistName != key:
                        print(song.artist.artistName, "!=", key)
                        return "fucked"
        return "seems nothing wrong"

    def addToLibrary(self, source: str) -> None:
        """Need to complete."""
        for item in source:
            song = ID3(item)
            self.__songs.append(Song(song.tag.title, item, song.tag.album,
                                   self.__albums, song.tag.artist, self.__artists))
        pass

    def addTagsToSong(self, songTitle: str, artistName: str, *tags: Set[str]) -> None:
        """Tag to song."""
        # need to add check for versions of __songs. I mean should i just transfer albumName to it or?..
        for song in self.__songs:
            if songTitle == song.title & song.artist.artistName == artistName:
                for tag in tags:
                    song.userTags.add(tag)

    def addTagsToAlbum(self, albumName: str, artistName: str, *tags: Set[str]) -> None:
        """Tag to __songs of album."""
        # compositeKey[0] is albumName and compositeKey[1] is artistName
        for compositeKey, album in self.__albums.items():
            if (albumName == compositeKey[0]) and (artistName == compositeKey[1]):
                for song in album.__songs:
                    for tag in tags:
                        song.userTags.add(tag)

    def addTagsToArtist(self, artistName: str, *tags: Set[str]) -> None:
        """Tag to __songs by artist."""
        for artistNameKey, artist in self.__artists.items():
            if artistName == artistNameKey:
                for song in artist.__songs:
                    for tag in tags:
                        song.userTags.add(tag)

    def deleteTagsFromSong(self, title: str, artistName: str, *tags: Set[str]) -> None:
        """Delete tag from song."""
        for song in self.__songs:
            if (title == song.title) and (artistName == song.artist.artistName):
                if tags[0] != "clear":
                    for tag in tags:
                        if tag in song.userTags:
                            song.userTags.remove(tag)
                else:
                    song.userTags.clear()

    def deleteTagsFromAlbum(self, albumName: str, artistName: str, *tags: Set[str]) -> None:
        """Delete tag from album."""
        # compositeKey[0] is albumName and compositeKey[1] is artistName
        for compositeKey, album in self.__albums.items():
            if (albumName == compositeKey[0]) and (artistName == compositeKey[1]):
                if tags[0] != "clear":
                    for song in album.__songs:
                        for tag in tags:
                            if tag in song.userTags:
                                song.userTags.remove(tag)
                else:
                    for song in album.__songs:
                        song.userTags.clear()

    def deleteTagsFromArtist(self, artistName: str, *tags: Set[str]) -> None:
        """Delete tag from artist."""
        for artistNameKey, artist in self.__artists.items():
            if artistName == artistNameKey:
                if tags[0] != "clear":
                    for song in artist.__songs:
                        for tag in tags:
                            if tag in song.userTags:
                                song.userTags.remove(tag)
                else:
                    for song in artist.__songs:
                        song.userTags.clear()

    def getNumberOfSongs(self) -> int:
        """Get amount of __songs in library."""
        return len(self.__songs)

    def updateID3toArtist(self, artistName: str) -> None:
        """doc."""
        pass
        # artist: Artist
        # for artistNameKey, artist in self.__artists.items():
        #     if artistName == artistNameKey:
        #         for song in artist.__songs:
        #             songID3 = ID3(song.path)

    def updateID3toAlbum(self, albumName: str) -> None:
        """doc."""
        pass

    def updateID3toSong(self, songTitle: str) -> None:
        """doc."""
        pass

    def hideAuxiliaryArtists():
        """Doc."""
        pass

    # ################### Below will be functions for testing and debugging library ##########################
    def printListOfArtists(self) -> None:
        """doc."""
        counter = 0
        for key, artist in self.__artists.items():
            counter += 1
            print(f"{counter} {artist.artistName}", end="\n")