from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),
    path("item/<slug:slug>", views.product_detail, name="product_detail"),
    path('shop/<slug:category_slug>/', views.category_list, name='category_list'),
    path('login/', views.login, name='login'),
    path('about/', views.about, name='about'),
    path('all-products', views.all, name='all-products'),
]