from django.contrib import admin
from .models import Categorie,Tache
# Register your models here.

class AdminCategorie(admin.ModelAdmin):
    list_display = ['nom']
    search_fields = ['nom']

class AdminTache(admin.ModelAdmin):
    list_display = ['nom','categorie','statut']
    search_fields = ['nom','statut']
    list_editable = ['statut']



admin.site.register(Categorie,AdminCategorie)
admin.site.register(Tache,AdminTache)