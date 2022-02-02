from django.db import models
from forum.models import Category,PubTags
# Create your models here.


class Pblog(models.Model):
    post_title = models.CharField(max_length=255,null=True)
    pub_categorie = models.ForeignKey(Category,null=True,on_delete=models.SET_NULL)
    #post_img = models.ImageField(upload_to='blog',null=True)
    pub_tags = models.ManyToManyField(PubTags)
    post_content = models.TextField(null=True)
    post_date = models.DateTimeField(auto_now_add=True,null=True)
    post_author = models.CharField(max_length=255,null=True)
    post_ua = models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.post_title
class Pmusik(models.Model):
    post_titre = models.CharField(max_length=255,null=True)
    post_categorie = models.ForeignKey(Category,null=True,on_delete=models.SET_NULL)
    post_pays = models.CharField(max_length=255, null=True)
    post_annee = models.DateField(max_length=255, null=True)
    post_artiste = models.CharField(max_length=255, null=True)
    post_description = models.CharField(max_length=255, null=True)
    #post_img = models.ImageField(upload_to='covers', null=True)
    post_author = models.CharField(max_length=255, null=True)
    post_date = models.DateTimeField(auto_now_add=True, null=True)
    post_ua = models.CharField(max_length=255, null=True)
    def __str__(self):
        return self.post_titre

class fichiers(models.Model):
    file = models.FileField(upload_to='multimedias')
    file_type = models.CharField(max_length=255,null=True)
    file_size = models.CharField(max_length=255,null=True)
    file_kind = models.CharField(max_length=255,null=True)
    file_post_author = models.CharField(max_length=255,null=True)
    file_post_id = models.BigIntegerField()
    file_upload_date = models.DateTimeField(auto_now_add=True,null=True)
    file_duration = models.CharField(max_length=255,null=True)
    file_original_name = models.CharField(max_length=255,null=True)
    file_post_ua = models.CharField(max_length=255,null=True)
    def __str__(self):
        return self.file_original_name