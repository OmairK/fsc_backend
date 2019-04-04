from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('user-profile-list/', views.UserProfileSearch.as_view(), name='user-profile-list'),
    path('user-profile-create/', views.CreateUserProfile.as_view(), name='user-profile-create'),
]
