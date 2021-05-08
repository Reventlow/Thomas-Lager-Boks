"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    #path('', views.todo, name='todo'),
    path('customer_list', views.customer_list, name='customer_list'),
    path('create_customer', views.create_customer, name='create_customer'),
    path('delete_customer/<customer_id>', views.delete_customer, name='delete_customer'),
    path('edit_customer/<customer_id>', views.edit_customer, name='edit_customer'),
    path('storageCenter_list', views.storageCenter_list, name='storageCenter_list'),
    path('create_storageCenter', views.create_storageCenter, name='create_storageCenter'),
    path('edit_storageCenter/<storageCenter_id>', views.edit_storageCenter, name='edit_storageCenter'),
    path('delete_storageCenter/<storageCenter_id>', views.delete_storageCenter, name='delete_storageCenter'),
]