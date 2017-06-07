#django import 
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView


urlpatterns = [
    # urls para la aplicacion home
    url(r'^admin/', admin.site.urls),
    #urls para home
    url(r'^', include('applications.home.urls', namespace="home_app")),
    #urls para users
    url(r'^', include('applications.users.urls', namespace="users_app")),
    # urls para la aplicacion item
    # url(r'^', include('applications.item.urls', namespace="item_app")),
    # urls para la aplicacion proceso
    url(r'^', include('applications.proceso.urls', namespace="proceso_app")),
    # urls para la aplicacion subproceso
    url(r'^', include('applications.subproceso.urls', namespace="subproceso_app")),
    # urls para la aplicacion miscelanea
    # url(r'^', include('applications.miscelanea.urls', namespace="miscelanea_app")),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
