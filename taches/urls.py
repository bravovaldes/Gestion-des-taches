from django.urls import include, path

from taches import views

urlpatterns = [
     path('',views.index,name='index'),
     path('dashboard',views.dashboard,name='dashboard')
]
