from django.db import models

class PubTags(models.Model):
    tag = models.CharField(max_length=255,null=True)
    def __str__(self):
        return self.tag
class Category(models.Model):
    valeurs = models.CharField(max_length=255, null=True)
    def __str__(self):
        return self.valeurs

class ForumModel(models.Model):
    post = models.TextField(null=True)
    pub_categorie = models.ForeignKey(Category,null=True,on_delete=models.SET_NULL)
    pub_date = models.DateTimeField(auto_now_add=True,null=False)
    pub_author = models.CharField(max_length=255,null=True)
    pub_tags = models.ManyToManyField(PubTags)
    def __str__(self):
        return self.post