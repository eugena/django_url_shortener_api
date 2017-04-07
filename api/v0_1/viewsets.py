# ViewSets define the view behavior.
from rest_framework import viewsets, status, response

from serializers import LinkSerializer
from shortener.models import Link
from utils import get_url


class LinkViewSet(viewsets.ModelViewSet):
    """
    Viewset for Link Model
    """
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

    def create(self, request, *args, **kwargs):
        """
        Adds a new url and returns the corresponding short url
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(
            {
                'short_url': get_url(self.request, serializer.data['code']), },
            status=status.HTTP_201_CREATED,
            headers=headers)

    def list(self, request, *args, **kwargs):
        """
        Outputs the list of links
        """
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        data = []
        for link in serializer.data:
            link['short_url'] = get_url(self.request, link['code'])
            data.append(link)
        return response.Response(data)
