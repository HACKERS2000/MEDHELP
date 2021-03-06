"""medbay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from health.views import (  index,
                            brain,
                            scrabble,
                            fourinrow,
                            connect4,
                            game,
                            slide_game,
                            game1)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('brain_games',brain),
    # path('fourinrow/',fourinrow),
    path('scrabble/',scrabble),
    path('connect4/',connect4),
    path('game/',game),
    path('slide_game/',slide_game),
    path('game1/',game1),


]
