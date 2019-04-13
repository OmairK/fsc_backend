from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls import url


urlpatterns = [
    path('user-profile-list/', views.UserProfileSearch.as_view(), name='user_profile_list'),
    path('user-profile-create/', views.CreateUserProfile.as_view(), name='user_profile_create'),
    url(r'^user-profile-update/(?P<player_id>\d+)$',views.UpdateUserProfile.as_view(), name ='user_profile_update'),
]
