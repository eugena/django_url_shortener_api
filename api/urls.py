from django.conf.urls import include, url
from rest_framework_swagger.views import get_swagger_view

from api.v0_1 import __version__ as __version_0_1__

schema_view = get_swagger_view(title='URL shortener API')

urlpatterns = [
    url(r'^%s/' % __version_0_1__, include("api.v0_1.urls")),
    url(r"^docs/", schema_view),
]
