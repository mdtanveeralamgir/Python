from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), #root path, dont do index().
    path('new/', views.new) #root path, dont do index().
]