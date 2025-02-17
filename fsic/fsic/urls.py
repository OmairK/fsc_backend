"""fsic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from rest_framework import routers
from users import views as user_views
from rest_framework.authtoken import views as authentication_views
from rest_framework.documentation import include_docs_urls
from django.conf.urls.static import static

from django.conf import settings
router = routers.DefaultRouter()

urlpatterns = [
    path('users/', include('users.urls')),
    path('form/',include('form_to_email.urls')),
    path('admin/', admin.site.urls),
    path('tournaments/',include('tournaments.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('docs/', include_docs_urls(title='FSC API endpoints')),
    path('', include(router.urls)),
    path('api-token-auth/',authentication_views.obtain_auth_token, name = 'api-token-auth'),
        
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


