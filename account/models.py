from django.db import models
# Create your models here.
class accountManagement(models.Model) :
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    email = models.EmailField()
    motDePasse = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100,null=True)
    date_inscription = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nom