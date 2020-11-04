from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('<int:pk>/remove/', views.remove, name='remove')
]