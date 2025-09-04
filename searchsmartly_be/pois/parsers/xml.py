import xml.etree.ElementTree as ET
from typing import Iterator

from pois.domain import Poi, Coordinates
from .base import BaseParser


class XmlParser(BaseParser):
    def get_poi_iterator(self, file_path: str) -> Iterator[Poi]:
        context = ET.iterparse(file_path, events=("start", "end"))
        context = iter(context)
        event, root = next(context)

        for event, elem in context:
            if event == "end" and elem.tag == "DATA_RECORD":
                try:
                    ratings_str = elem.find("pratings").text or ""
                    ratings = (
                        [int(r) for r in ratings_str.split(",")] if ratings_str else []
                    )
                    avg_rating = sum(ratings) / len(ratings) if ratings else 0

                    yield Poi(
                        external_id=elem.find("pid").text,
                        name=elem.find("pname").text,
                        category=elem.find("pcategory").text,
                        coordinate=Coordinates(
                            latitude=float(elem.find("platitude").text),
                            longitude=float(elem.find("plongitude").text),
                        ),
                        average_rating=avg_rating,
                        ratings=ratings,
                        source_path=file_path,
                    )
                    root.clear() # Free up memory
                except (AttributeError, ValueError) as e:
                    print(f"Skipping malformed record. Error: {e}")
                    continue
