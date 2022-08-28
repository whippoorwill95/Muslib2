"""doc."""


from Library.Album import Album
from Library.Song import Song
from Library.Artist import Artist
from Library.UserTag import UserTag
from Library.LibraryAlbum import LibraryAlbum
from Library.LibrarySong import LibrarySong
from Library.LibraryArtist import LibraryArtist
from Library.LibraryUserTag import LibraryUserTag
import pickle


# Сначала из ссылки на файл создаем объекты классов альбом песня артист без юзер тага пока что
# Затем из объектов создаем объекты библиотеку ну то есть тупо кладем в множество
# Затем эти множества складируем в файл используя pickle
# И в обратном порядке при запуске файла или отдельной команды собираем объекты библиотек из файла и тестим результат
# для этого мне надо реализовать какой то print


path = r"M:\Sun Leads Me On"
