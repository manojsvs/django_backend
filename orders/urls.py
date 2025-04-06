from django.urls import path
from . import views

urlpatterns = [
    path('log_order/', views.log_order, name='log_order'),
    path('show_orders/', views.show_orders, name='show_orders'),
    path('clear_orders/', views.clear_orders, name='clear_orders'),
]
