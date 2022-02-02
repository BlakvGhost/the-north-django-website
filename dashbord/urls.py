from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="dash"),
    path('publish/blog/', views.blog, name="publishBlog"),
    path('publish/musique/', views.musique, name="publishMsq"),
    path('upload/',views.upload,name='upload'),
    path('demo/',views.demo,name='demo'),
]
