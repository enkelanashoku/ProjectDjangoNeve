from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),    
    path('gallery/', views.gallery, name='gallery'),
    path('services/', views.services, name='services'),
    path('products/', views.products, name='products'),
    path('products/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('book/', views.book, name='book'),
    path('appointment/', views.book, name='appointment'),
]
