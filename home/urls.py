from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
     path('view_scents', views.view_scents, name='view_scents'),
]
