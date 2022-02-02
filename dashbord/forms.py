from django import forms
from django.forms import ModelForm
from .models import Pblog,fichiers,Pmusik
class Blog(forms.ModelForm):
    post_title = forms.CharField(label='Post Titre', widget=forms.TextInput(attrs={'class': 'form-control','required':'True'}))
    class Meta:
        model = Pblog
        fields = ['post_title','pub_categorie','pub_tags']

class Musique(forms.ModelForm):
    post_annee = forms.CharField(label='Post Annee',widget=forms.DateInput(attrs={'type': 'date', 'required':
        'True'}))
    class Meta:
        model = Pmusik
        fields = ['post_titre','post_categorie','post_pays','post_annee','post_artiste','post_description']

class Files(ModelForm):
    class Meta:
        model = fichiers
        fields = ['file']