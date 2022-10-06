"""doc."""


from mutagen.id3 import ID3, ID3NoHeaderError
from Library.Song import Song
# from collections import deque
# this shit is broken what deque is?


# It's a plug
from Utils.Search import find
import logging
import logging.config
from logs.settings import logger_config
logging.config.dictConfig(logger_config)
logger = logging.getLogger('app_logger')


class Library:
    """doc."""

    def __init__(self, source=None):
        """doc. Source should be dir."""
        self.songs = list()
        self.albums = dict()
        self.artists = dict()
        if source is not None:
            for item in find(source, "*.[mf][pl][3a]*"):
                try:
                    song = ID3(item)
                    self.songs.append(Song(song["TIT2"].text[0], item, song["TALB"].text[0],
                                      self.albums, song['TPE1'].text[0], self.artists))
                except:
                    logger.exception(f'item = {item}')
                    pass

    def aplyTagToAllLibrary(self, tagName: str) -> None:
        """doc."""
        for song in self.songs:
            song.userTags.add(tagName)

    def makePlaylistFromUserTag(self, tagName: str) -> None:
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

    def checkArtistNamesOnCaseDiversity(self) -> str:
        """doc."""
        for song in self.songs:
            for key in self.artists.keys():
                if song.artist.artistName.lower() == key.lower():
                    if song.artist.artistName != key:
                        print(song.artist.artistName, "!=", key)
                        return "fucked"
        return "seems nothing wrong"

    # def addToLibrary(self, source: str) -> None:
    #     """Add to library."""
    #     for item in find(source, "*.[mf][pl][3a]*"):
    #         song = eyed3.load(item)
    #         self.songs.append(Song(song.tag.title, item, song.tag.album,
    #                                self.albums, song.tag.artist, self.artists))

    def aplyTagToSong(self, title: str, artistName: str, tagName: str) -> None:
        """Tag to song."""
        # need to add check for versions of songs. I mean should i just transfer albumName to it or?..
        for song in self.songs:
            if title == song.title & song.artist.artistName == artistName:
                song.userTags.add(tagName)

    def aplyTagToAlbum(self, albumName: str, tagName: str) -> None:
        """Tag to songs of album."""
        for album in self.albums:
            if albumName == album.albumName:
                for song in album.songs:
                    song.userTags.add(tagName)

    def aplyTagToArtist(self, artistName: str, tagName: str) -> None:
        """Tag to songs by artist."""
        for artist in self.artists:
            if artistName == artist.artistName:
                for song in artist.songs:
                    song.userTags.add(tagName)

    def deleteTagFromSong(self, title: str, artistName: str, tagName: str) -> None:
        """Delete tag from song."""
        for song in self.songs:
            if (title == song.title) & (artistName == song.artist.artistName):
                if tagName in song.userTags:
                    song.userTags.remove(tagName)

    def deleteTagFromAlbum(self, albumName: str, tagName: str) -> None:
        """Delete tag from album."""
        for album in self.albums:
            if albumName == album.albumName:
                for song in album.songs:
                    if tagName in song.userTags:
                        song.userTags.remove(tagName)

    def deleteTagFromArtist(self, artistName: str, tagName: str) -> None:
        """Delete tag from artist."""
        for artist in self.artists:
            if artistName == artist.artistName:
                for song in artist.songs:
                    if tagName in song.userTags:
                        song.userTags.remove(tagName)

    def getNumberOfSongs(self) -> int:
        """Get amount of songs in library."""
        return len(self.songs)

    def hideAuxiliaryArtists():
        """Doc."""
        pass
