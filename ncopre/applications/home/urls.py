from django.conf.urls import include, url
from . import views

urlpatterns = [
    # urls para la aplicacion home
    url(
        r'^templates/$',
        views.IndexView.as_view(),
        name='index'
    ),

]
