from django.conf.urls import url, include

# local
from . import views
urlpatterns = [
    #urls para vistas




    #urls para viewsets
    url(
        r'^',
        include(
            'applications.users.services_urls',
            namespace="users_servis_url"
        )
    ),
]
