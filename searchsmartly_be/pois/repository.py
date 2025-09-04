from typing import List

from django.contrib.gis.geos import Point

from .domain import Poi as PoiDomain
from .models import Poi as PoiModel


class PoiRepository:

    def bulk_create(self, pois: List[PoiDomain]) -> int:
        poi_models = [
            PoiModel(
                external_id=poi.external_id,
                name=poi.name,
                category=poi.category,
                coordinate=Point(poi.coordinate.longitude, poi.coordinate.latitude, srid=4326),
                ratings=poi.ratings,
                average_rating=poi.average_rating,
                description=poi.description,
                source_path=poi.source_path,
            )
            for poi in pois
        ]

        created_objects = PoiModel.objects.bulk_create(poi_models, batch_size=1000, ignore_conflicts=True)
        return len(created_objects)
