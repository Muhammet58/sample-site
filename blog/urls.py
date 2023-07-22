from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('comunication', views.communication, name='communication'),
    path('blog_details/<slug:slug>',views.blog_details, name='blog_details')
]