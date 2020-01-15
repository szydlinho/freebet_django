import django_filters
from .models import Matches_Pred


class MatchesListFilter(django_filters.FilterSet):
    class Meta:
        model = Matches_Pred
        fields = {
            'model': ['exact', 'contains'],
            'league': ['exact', 'contains'],
        }