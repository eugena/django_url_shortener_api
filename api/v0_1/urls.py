from django.conf.urls import url, include

from viewsets import LinkViewSet
from routers import LinkRouter


router = LinkRouter()
router.register(r'', LinkViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
