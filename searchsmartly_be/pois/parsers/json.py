import json
from typing import Iterator

from pois.domain import Poi, Coordinates
from .base import BaseParser


class JsonParser(BaseParser):
    def get_poi_iterator(self, file_path: str) -> Iterator[Poi]:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        for item in data:
            try:
                ratings = item.get("ratings", [])
                avg_rating = sum(ratings) / len(ratings) if ratings else 0

                yield Poi(
                    external_id=item["id"],
                    name=item["name"],
                    category=item["category"],
                    coordinate=Coordinates(
                        latitude=item["coordinates"]["latitude"],
                        longitude=item["coordinates"]["longitude"],
                    ),
                    description=item.get("description"),
                    average_rating=avg_rating,
                    ratings=ratings,
                    source_path=file_path,
                )
            except (KeyError, TypeError) as e:
                print(f"Skipping malformed record: {item}. Error: {e}")
                continue
