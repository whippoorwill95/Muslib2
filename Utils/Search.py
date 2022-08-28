"""doc."""

import glob


def find(path, mask):
    """Поиск."""
    # тут две звездочки для рекурсивного поиска, то есть мы заходим в срк и ищем во всех папках внутри
    return glob.glob(f"{path}/**/{mask}", recursive=True)
