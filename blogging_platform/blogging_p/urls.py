from django.urls import path
from . import views

urlpatterns = [  # Define your app's URL patterns
    path('' , views.product_list, name='product_list'),  # Define your app's URL patterns
    path('product/<int:id>/', views.product_detail, name='product_detail'),  # Define your app's URL patterns
    path('<int:pk>/edit/', views.edit_product, name='edit_product'),
    path('<int:pk>/delete/', views.delete_product, name='delete_product'),
]