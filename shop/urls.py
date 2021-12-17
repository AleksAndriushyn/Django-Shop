from django.urls import path, re_path

from . import views

app_name = 'shop'
urlpatterns = [
    re_path(r'^shop_register$', views.RegisterFormView.as_view(), name='shop-register'),
    re_path(r'^shop_login$', views.LoginFormView.as_view(), name='shop-login'),
    re_path(r'^logout', views.LogoutView.as_view(), name='logout'),
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_filtered'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]