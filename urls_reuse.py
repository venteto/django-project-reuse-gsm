"""
URL configuration for ___ project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage 
from django.urls import include, path
from django.views.generic.base import RedirectView

'''  admin/base_site.html override template also affects the title '''
admin.site.site_title = 'REAL Django Admin'   # DEFAULT: "Django site admin"
admin.site.site_header = 'Real Django Admin'  # DEFAULT: "Django Administration"
admin.site.index_title = 'Site Admin Home'    # DEFAULT: "Site Administration"


urlpatterns = [
    path(settings.ADMIN_PATH, admin.site.urls),

    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url(
        'favicons/favicon-32x32.png'), permanent=True)),

    # path('accounts/', include('django.contrib.auth.urls')),
]
