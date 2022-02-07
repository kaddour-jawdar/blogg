from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('single/<int:pk>', views.new_single, name='new_single'),
]