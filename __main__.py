"""doc."""


# from Library.Album import Album
# from Library.Song import Song
# from Library.Artist import Artist
# from Library.UserTag import UserTag
from Library.Library import Library
# from Library.LibraryUserTag import LibraryUserTag
import pickle


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
library.makePlaylistFromUserTag("Listen-Friendly")

#             if records.index(i) != len(records)-1:
#                 file.write(i[0] + "\n")
#             else:
#                 file.write(i[0])
