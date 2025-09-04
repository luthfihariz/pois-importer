from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Coordinates:
    latitude: float
    longitude: float


@dataclass
class Poi:
    external_id: str
    name: str
    category: str
    coordinate: Coordinates
    average_rating: float
    description: Optional[str] = None
    ratings: List[int] = field(default_factory=list)
    source_path: Optional[str] = None
