from importlib.metadata import PackageNotFoundError, version

from epitran._epitran import Epitran
from epitran.reromanize import ReRomanizer

try:
    __version__ = version("epitran")
except PackageNotFoundError:
    # package is not installed
    pass

__all__ = ["Epitran", "ReRomanizer"]
