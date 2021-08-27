from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('accounts/login/', views.Login.as_view(), name='login'),
  path('rooftops/', views.rooftops_index, name='rooftops_index'),
  path('rooftops/<int:rooftop_id>/', views.rooftops_detail, name='rooftops_detail'),
  path('rooftops/create/', views.RooftopCreate.as_view(), name='rooftops_create'),
  path('rooftops/<int:pk>/update/', views.RooftopUpdate.as_view(), name='rooftops_update'),
  path('rooftops/<int:pk>/delete/', views.RooftopDelete.as_view(), name='rooftops_delete'),
  path('rooftops/<int:rooftop_id>/add_photo/', views.add_photo, name='add_photo'),
]