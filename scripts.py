"""Scripts for personal use mostly."""


# I use TYPE_CHECCKING to use type hints without getting circular import error
from typing import TYPE_CHECKING
from os import path
import pickle


if TYPE_CHECKING:
    from Library.Library import Library


def main():
    """fuck."""
    basepath = path.dirname(__file__)
    filepath = path.abspath(path.join(basepath, "library.pickle"))
    with open(filepath, 'r+b') as f:
        library = pickle.load(f)
    # library.addTagsToSong("Tourist", "Julian Casablancas", "Zaglushka")
    # library.addTagsToArtist("Bohren & der Club of Gore", "background")
        library.printListOfArtists()

        pickle.dump(library, f)


if __name__ == "__main__":
    main()
