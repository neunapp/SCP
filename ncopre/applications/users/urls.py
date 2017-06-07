from django.conf.urls import url, include

# local
from . import views
urlpatterns = [
    #urls para vistas
    url(r'^$',
        views.LogInView.as_view(),
        name='login'
    ),



    #urls para viewsets
    url(
        r'^',
        include(
            'applications.users.services_urls',
            namespace="users_servis_url"
        )
    ),
]
