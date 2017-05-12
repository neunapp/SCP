"""ncopre URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView


urlpatterns = [
    # urls para la aplicacion home
    url(r'^admin/', admin.site.urls),
    url(r'^', include('applications.home.urls', namespace="home_app")),
    # urls para la aplicacion item
    # url(r'^', include('applications.item.urls', namespace="item_app")),
    # urls para la aplicacion proceso
    url(r'^', include('applications.proceso.urls', namespace="proceso_app")),
    # urls para la aplicacion subproceso
    # url(r'^', include('applications.subproceso.urls', namespace="subproceso_app")),
    # urls para la aplicacion miscelanea
    # url(r'^', include('applications.miscelanea.urls', namespace="miscelanea_app")),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
