from django.urls import path
from . import views

urlpatterns = [
    path('recommend/', views.get_recommendations, name='get_recommendations'),
]
