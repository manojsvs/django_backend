from django.urls import path
from . import views

urlpatterns = [
    path('log_food_order/', views.log_food_order, name='log_food_order'),
    path('view_food_orders/', views.view_food_orders, name='view_food_orders'),
    path('clear_food_orders/', views.clear_food_orders, name='clear_food_orders'),
]
