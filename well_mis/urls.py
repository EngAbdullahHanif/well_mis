"""well_mis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from well import views  
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('advanced_filters', include('advanced_filters.urls')),
    # url(r'^export-exl/$', views.export, name='export'),
    # url(r'^export-csv/$', views.export, name='export'),
    # url(r'^import/$', views.simple_upload, name='import'),
]


 
