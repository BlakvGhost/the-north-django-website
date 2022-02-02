from django.urls import path
from . import views

urlpatterns = [
    path('inscription/',views.inscription,name='inscription'),
    path('connexion/',views.connexion,name='connexion'),
    path('logout',views.logoutUser,name='logout'),
]