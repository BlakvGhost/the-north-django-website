from django.forms import ModelForm
from .models import LesCommentaires

class CommentForm(ModelForm):
    class Meta:
        model = LesCommentaires
        fields = ['comment']