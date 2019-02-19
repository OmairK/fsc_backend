from django.urls import path, include
from . import views

urlpatterns = [
    path('api/user/', views.UserCreate.as_view(), name='account-create'),
]
