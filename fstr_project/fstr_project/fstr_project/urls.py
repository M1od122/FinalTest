"""
URL configuration for fstr_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include

from .views import submit_data, get_pass, edit_pass, get_user_passes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('fstr_app.urls')),
    path('submitData/', submit_data, name='submit_data'),
    path('submitData/<int:id>/', get_pass, name='get_pass'),
    path('submitData/edit/<int:id>/', edit_pass, name='edit_pass'),
    path('submitData/', get_user_passes, name='get_user_passes'),
]
