from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('user-profile/', views.UserProfileSearch.as_view(), name='user-profile'),
    
]
