from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('rooftops/', views.rooftops_index, name='rooftops_index'),
  path('rooftops/<int:rooftop_id>/', views.rooftops_detail, name='rooftops_detail'),
]