from django.urls import path
from . import views
app_name = 'home'

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('<slug:slug>', views.product_detail, name='product_detail'),
    path('search/<slug:category_slug>/', views.category_list, name='category_list'),
    path('contact/', views.contact_register, name='contact'),
    path('about/', views.about_page, name='about'),
    path('mission/', views.mission_page, name='mission'),
    path('vision/', views.vision_page, name='vision'),
    path('location/', views.location_page, name='location'),
  
]