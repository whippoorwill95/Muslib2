"""doc."""


# import Song from Song
# import Artist from Artist
# import UserTag from UserTag

class Album:
    """doc."""

    def __init__(self, song, artist, name):
        """doc."""
        self.albumName = name
        # self.userTags = set()
        self.songs = {song}
        self.artist = artist

    def addSong(self, song):
        """doc."""
        self.songs.add(song)
    # @property
    # def song(self):
    #     return self._song

    # @song.setter
    # def song(self, song):
    #     self._song = song

    # Songs = []
    # list with References to Song object

    # Artist =
    # Reference to an Artist object

    # UserTags = set()
    # Set of Usertags
