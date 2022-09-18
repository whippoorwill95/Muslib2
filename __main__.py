"""doc."""


from Library.Library import Library
import pickle
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QTableWidget
)

WINDOW_SIZE = 800


class LibWindow(QMainWindow):
    """Main window (GUI or view)."""

    def __init__(self):
        """Doc."""
        super().__init__()
        self.setWindowTitle("MusicLib2")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        self._createTable()

    def _createTable(self):
        self.table = QTableWidget()


def main():
    """Start application."""
    musicLibApp = QApplication([])
    musicLibWindow = LibWindow()
    musicLibWindow.show()
    sys.exit(musicLibApp.exec())


if __name__ == "__main__":
    main()
# Сначала из ссылки на файл создаем объекты классов альбом песня артист без юзер тага пока что
# Затем из объектов создаем объекты библиотеку ну то есть тупо кладем в множество
# Затем эти множества складируем в файл используя pickle
# И в обратном порядке при запуске файла или отдельной команды собираем объекты библиотек из файла и тестим результат
# для этого мне надо реализовать какой то print


# path = r"M:\music\m3"

# newlib = Library(path)
# for song in newlib.songs:
#     print(song.songName, song.album.albumName, song.artist.artistName)

# for key, album in newlib.albums.items():
#     for song in album.songs:
#         print(song.songName)

# newlib.aplyTagToAllLibrary("Listen-Friendly")
# with open('library.pickle', 'wb') as f:
#   pickle.dump(newlib, f)
with open('library.pickle', 'rb') as f:
    library = pickle.load(f)
# library.makePlaylistFromUserTag("Listen-Friendly")
# print(library.checkArtistNamesOnCaseDiversity())

#             if records.index(i) != len(records)-1:
#                 file.write(i[0] + "\n")
#             else:
#                 file.write(i[0])
