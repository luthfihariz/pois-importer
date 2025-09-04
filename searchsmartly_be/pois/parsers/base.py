from abc import ABC, abstractmethod
from typing import Iterator

from pois.domain import Poi


class BaseParser(ABC):
    @abstractmethod
    def get_poi_iterator(self, file_path: str) -> Iterator[Poi]:
        pass
