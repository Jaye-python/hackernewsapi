"""hackernews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
    
    path('', views.Home.as_view(), name='home'),

    path('seedthedb/', views.seedTheDB, name='seedthedb'),  # SEED THE DATABASE. TO BE USED ONLY ONCE

    path('news/<action>/', views.Home.as_view(), name='home'),
    
    path('details/<pk>/', views.NewsDetail.as_view(), name='details'),

    path('delete/<hacker_id>/', views.deleteNews, name='delete'),

    
    

]
