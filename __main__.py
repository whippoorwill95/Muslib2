"""doc."""


# import pickle
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QTableWidget,
    QTableWidgetItem
)
from Library.Library import Library
# from PyQt6.QtCore import Qt
# I use TYPE_CHECCKING to use type hints without getting circular import error
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from Library.Song import Song


class LibWindow(QMainWindow):
    """Main window (GUI or view)."""

    def __init__(self, library):
        """Doc."""
        super().__init__()
        self.setWindowTitle("MusicLib2")
        self.setGeometry(0, 30, 1000, 600)
        generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(generalLayout)
        self.setCentralWidget(centralWidget)

        table = QTableWidget()
        table.setColumnCount(3)
        table.setRowCount(library.getNumberOfSongs())
        table.setHorizontalHeaderLabels(["Title", "Album", "Artist"])
        table.resizeColumnsToContents()

        row = 0
        song: 'Song'
        for song in library.songs:
            table.setItem(row, 0, QTableWidgetItem(song.title))
            table.setItem(row, 1, QTableWidgetItem(song.album.albumName))
            table.setItem(row, 2, QTableWidgetItem(song.artist.artistName))
            row += 1

        generalLayout.addWidget(table)


def main():
    """Start application."""
    # with open('library.pickle', 'rb') as f:
    #    library = pickle.load(f)
    path = r"M:\music\m4\Таня Буланова"
    library = Library(path)
    musicLibApp = QApplication([])
    musicLibWindow = LibWindow(library)
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
# library.makePlaylistFromUserTag("Listen-Friendly")
# print(library.checkArtistNamesOnCaseDiversity())

#             if records.index(i) != len(records)-1:
#                 file.write(i[0] + "\n")
#             else:
#                 file.write(i[0])
