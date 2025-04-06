from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('orders/', include('orders.urls')),
    path('restaurant/', include('restaurant.urls')),  #  New restaurant route
]
