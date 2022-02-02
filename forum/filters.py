import django_filters
from .models import ForumModel

class ForumFilter(django_filters.FilterSet):
    class Meta:
        model= ForumModel
        fields = '__all__'
        exclude = ['pub_categorie','pub_tags']