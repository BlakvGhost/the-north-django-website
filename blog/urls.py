from django.urls import path
from . import views

urlpatterns = [
    path('',views.blog,name='indexblog'),
    path('detail/<int:pk>/',views.detail,name='blogdetail'),
]