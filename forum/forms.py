from django.forms import ModelForm
from .models import ForumModel

class ForumForm(ModelForm):
    class Meta:
        model = ForumModel
        fields = ['pub_tags','pub_categorie','post']