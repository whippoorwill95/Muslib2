"""doc."""


from abc import (ABC)
import eyed3


class LibraryABC(ABC):
    """doc."""

    @property
    def TagObject(self, path):
        """doc."""
        try:
            eyed3object = eyed3.load(path)
            return eyed3object.tag
        except eyed3.Error:
            print("Error on reading tags")
