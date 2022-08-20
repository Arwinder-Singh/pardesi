import django_filters

from accounts.models import Room


class Filter(django_filters.FilterSet):
    class Meta:
        model=Room
        fields=['category','city','price','availablity','amenities']