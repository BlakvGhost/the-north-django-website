from django.db import models

# Create your models here.
class LesCommentaires(models.Model):
    comment = models.TextField(null=True)
    comment_categorie = models.CharField(max_length=100,null=True)
    comment_date = models.DateTimeField(auto_now_add=True,null=False)
    comment_author = models.CharField(max_length=255,null=True)
    comment_to = models.BigIntegerField(null=True)
    comment_type = models.CharField(max_length=30,default='just comment')
    comment_replyedTo = models.CharField(max_length=255,null=True)
    def __str__(self):
        return self.comment