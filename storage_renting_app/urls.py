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
    #path('cross_off/<job_id>', views.cross_off, name='cross_off'),
    #path('uncross/<job_id>', views.uncross, name='uncross'),
    #path('edit/<job_id>', views.edit, name='edit'),
]