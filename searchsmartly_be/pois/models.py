from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.gis.db import models as gis_models


class Poi(models.Model):
    external_id = models.CharField(max_length=255, db_index=True)
    name = models.CharField(max_length=255)
    coordinate = gis_models.PointField(srid=4326, db_index=True)
    ratings = ArrayField(models.IntegerField(), default=list)
    category = models.CharField(max_length=255, db_index=True)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    description = models.TextField(null=True, blank=True)
    source_path = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        indexes = [
            gis_models.Index(fields=['coordinate'], name='poi_coordinate_idx'),
        ]
        constraints = [
            models.UniqueConstraint(fields=['source_path', 'external_id'], name='unique_source_external_id')
        ]
        db_table = 'pois'
        verbose_name = 'Point of Interest'
        verbose_name_plural = 'Points of Interest'
                

