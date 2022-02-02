from django.urls import path
from . import views

urlpatterns = [
    path('',views.forum,name='indexforum'),
    path("detail/<int:pk>/",views.details,name='forumdetail'),
    path("category/<str:ct>/",views.category,name='categoryforum'),
    path("recherche/",views.search,name='searchforum'),
    path('ajax/',views.ajax,name='ajax')
]