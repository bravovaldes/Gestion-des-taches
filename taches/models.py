from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    isdelete = models.BooleanField(default=False)
    
    class Meta:
        abstract = True
        
    
class Categorie(Base):
    nom =models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nom
    


class Tache(Base):
    CHOICES = (
    ('elever', 'Elever'),
    ('medium', 'Medium'),
    ('faible', 'Faible'),
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie,on_delete=models.CASCADE)
    nom =models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    statut = models.BooleanField(max_length=50)
    priorite = models.CharField(max_length=50,choices=CHOICES)
    debut = models.DateTimeField()
    fin = models.DateTimeField()
    slug = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nom