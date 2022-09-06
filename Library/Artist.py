"""doc."""

# from Library.Album import Album
# from Library.Song import Song


class Artist:
    """doc."""

    def __init__(self, song, name):
        """doc."""
        self.albums = set()
        self.songs = {song}
        self.artistName = name

    def addSong(self, song):
        """doc."""
        self.songs.add(song)

    def addAlbum(self, album):
        """doc."""
        self.albums.add(album)
    # Albums =
    # list with References to an Album object

    # Songs =
    # list with References to Song object
