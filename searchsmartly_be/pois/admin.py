from django.contrib import admin
from django.db.models import Q

from .models import Poi


@admin.register(Poi)
class PoiAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "external_id",
        "category",
        "average_rating",
    )
    search_fields = ("external_id",)
    list_filter = ("category",)

    def get_search_results(self, request, queryset, search_term):
        if not search_term:
            return queryset, False

        queryset = queryset.filter(Q(external_id=search_term) | Q(id=int(search_term)))

        return queryset, False
