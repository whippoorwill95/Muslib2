"""doc."""


import pickle
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QTableWidget,
    QTreeView,
    QTableWidgetItem
)
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QFont, QColor
from Library.Library import Library
# from PyQt6.QtCore import Qt
# I use TYPE_CHECCKING to use type hints without getting circular import error
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from Library.Song import Song


class StandartItem(QStandardItem):
    def __init__(self, text='', font_size=12, set_bold=False, color=QColor(0, 0, 0)):
        super().__init__()

        font = QFont("Open Sans", font_size)
        font.setBold(set_bold)

        self.setEditable(False)
        self.setForeground(color)
        self.setFont(font)
        self.setText(text)


class LibWindow(QMainWindow):
    """Main window (GUI or view)."""

    def __init__(self, library: Library = None):
        """Doc."""
        super().__init__()
        self.setWindowTitle("MusicLib2")
        self.setGeometry(0, 30, 1000, 600)
        generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(generalLayout)
        self.setCentralWidget(centralWidget)
        if library is not None:
            treeView = QTreeView()
            treeView.setHeaderHidden(True)
            treeModel = QStandardItemModel()
            rootNode = treeModel.invisibleRootItem()

            lfs = list(library.artists.items())
            for i in range(len(lfs)):
                # print(lfs[i][1].albums)
                self.__dict__[f'artist{i}'] = StandartItem(f'{lfs[i][0]}', 16, set_bold=True)
                # print((list(lfs[i][1].albums)))
                for a in range(len(albums := sorted(list(lfs[i][1].albums)))):
                    print(f'{albums[a].albumName}')
                    self.__dict__[f'album{i}_{a}'] = StandartItem(f'{albums[a].albumName}', 14)
                    self.__dict__[f'artist{i}'].appendRow(self.__dict__[f'album{i}_{a}'])
                    for t in range(len(songs := sorted(list(albums[a].songs)))):
                        self.__dict__[f'song{i}_{a}_{t}'] = StandartItem(f'{songs[t].title}', 12, color=QColor(155, 0, 0))
                        self.__dict__[f'album{i}_{a}'].appendRow(self.__dict__[f'song{i}_{a}_{t}'])
                rootNode.appendRow(self.__dict__[f'artist{i}'])

            treeView.setModel(treeModel)
            treeView.expandAll()
            self.setCentralWidget(treeView)
            # table = QTableWidget()
            # table.setColumnCount(4)
            # table.setRowCount(library.getNumberOfSongs())
            # table.setHorizontalHeaderLabels(["Title", "Album", "Artist", "UserTags"])
            # table.resizeColumnsToContents()

            # row = 0
            # song: 'Song'
            # for song in library.songs:
            #     table.setItem(row, 0, QTableWidgetItem(song.title))
            #     table.setItem(row, 1, QTableWidgetItem(song.album.albumName))
            #     table.setItem(row, 2, QTableWidgetItem(song.artist.artistName))
            #     table.setItem(row, 3, QTableWidgetItem(str(song.userTags)))
            #     row += 1

            # generalLayout.addWidget(table)


def main():
    """Start application."""
    #with open('library.pickle', 'rb') as f:
    #    library = pickle.load(f)
    path = r"M:\music\test"
    repattern = r'.*\.(mp3|flac|m4a)$'
    library = Library(regexPattern=repattern, source=path)
    # print(library.artists)
    # for a in library._Library__artists:
    #     print(library._Library__artists[a].artistName)
    # for s in library._Library__songs:
    #     print(f"Песня: {s.title}, Исполнитель: {s.artist}, альбом: {s.album}")

    musicLibApp = QApplication(sys.argv)
    musicLibWindow = LibWindow(library)
    musicLibWindow.show()
    #with open('library.pickle', 'wb') as f:
    #    pickle.dump(library, f)
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

    # filenames = list(filter(re.compile(repattern).match, os.walk(path)))
    # with open('debug.txt', 'w', encoding='utf-8') as f:
    #     for item in filenames:
    #         f.write(f"{item}\n")
    # with open('debug.txt', 'w', encoding='utf-8') as f:
    #     for address, dirs, files in os.walk(path):
    #         for name in files:
    #             f.write(f"{os.path.join(address, name)}\n")
    # with open('debug.txt', 'r', encoding='utf-8') as f:
    #     list = f.readlines()
    #     print(*(x for x in list if re.search(repattern, x)), sep='\n')
