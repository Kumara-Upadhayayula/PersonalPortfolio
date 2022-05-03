from django.urls import path
from . import views


urlpatterns = [
    path('', views.projects, name="home"),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
    path('contact/', views.contact, name='contact'),
    path('singleproject/<str:pk>', views.SingleProject, name="single-project"),

]
