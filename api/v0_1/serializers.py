# Serializers define the API representation.
from django.conf import settings
from rest_framework import serializers

from shortener.models import Link


class LinkSerializer(serializers.ModelSerializer):

    url = serializers.URLField()

    def create(self, validated_data):
        """
        Create a link

        Checks if a link exists and returns new or existing instance
        """
        ModelClass = self.Meta.model

        try:
            instance = ModelClass.objects.get(
                url=validated_data.get('url'),
                target=validated_data.get('target', settings.TYPE_DESKTOP))
        except ModelClass.DoesNotExist:
            instance = super(LinkSerializer, self).create(validated_data)
        return instance

    class Meta:
        model = Link
        fields = ('code', 'url', 'created', 'qty', 'target', )
