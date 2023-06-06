from django.urls import  path
from compte import views
urlpatterns = [
    path('inscription',views.inscription,name="login"),
    path('connexion',views.connexion,name='connexion'),
    path('deconnexion',views.deconnexion,name='deconnexion')
    
]
