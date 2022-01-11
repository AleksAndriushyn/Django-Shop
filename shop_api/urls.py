from django.urls import path

from . import views

app_name = 'shop_api'
urlpatterns = [
    path('products/', views.GetListAllProducts.as_view()),
    path('products/<int:pk>/', views.PostProduct.as_view()),
    path('categories/', views.GetListAllCategories.as_view()),
    path('categories/<int:pk>/', views.PostCategory.as_view()),
    path('orders/', views.GetListAllOrders.as_view()),
    path('orders/<int:pk>/', views.PostOrder.as_view()),
    path('order_items/', views.GetListAllOrderItems.as_view()),
    path('order_items/<int:pk>/', views.PostOrderItem.as_view()),
]
