import csv
from typing import Iterator

from pois.domain import Poi, Coordinates
from .base import BaseParser


class CsvParser(BaseParser):
    def get_poi_iterator(self, file_path: str) -> Iterator[Poi]:
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)  # Skip header
            for row in reader:
                try:
                    # Manually parse ratings from "{3.0,4.0,...}" format
                    ratings_str = row[5].strip("{}")
                    ratings = (
                        [int(float(r)) for r in ratings_str.split(",")]
                        if ratings_str
                        else []
                    )

                    avg_rating = sum(ratings) / len(ratings) if ratings else 0

                    yield Poi(
                        external_id=row[0],
                        name=row[1],
                        category=row[2],
                        coordinate=Coordinates(
                            latitude=float(row[3]), longitude=float(row[4])
                        ),
                        average_rating=avg_rating,
                        ratings=ratings,
                        source_path=file_path,
                    )
                except (ValueError, IndexError) as e:
                    print(f"Skipping malformed row: {row}. Error: {e}")
                    continue
