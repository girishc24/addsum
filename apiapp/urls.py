from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='members'),
    path('addsum/', views.Addsum.as_view())
]