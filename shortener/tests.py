from json import dumps
from django.test import TestCase
from django.test import Client
from django.conf import settings

from shortener.models import Link
from api.v0_1 import __version__ as __version_0_1__

SERVER_NAME = "short.io"


class LinkTestCase(TestCase):

    def setUp(self):
        self.client = Client(enforce_csrf_checks=True, SERVER_NAME=SERVER_NAME)
        self.google_link = Link.objects.create(
            url="http://www.google.com",
            target=settings.TYPE_TABLET)
        self.yahoo_link = Link.objects.create(url="http://www.yahoo.com")

    def test_link_model(self):
        """
        Model tests
        """
        self.assertEqual(self.google_link.target, settings.TYPE_TABLET)
        self.assertEqual(self.yahoo_link.target, settings.TYPE_DESKTOP)

    def test_get_list(self):
        """
        Getting the list of links
        """
        response = self.client.get(
            '/%s/' % __version_0_1__)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def test_create_link(self):
        """
        Creating a new link
        """
        link = "http://coursera.org"
        response = self.client.post(
            '/%s/' % __version_0_1__,
            dumps({"url": link}),
            content_type="application/json")
        self.assertEqual(response.status_code, 201)
        coursera_link = Link.objects.get(url=link)
        self.assertEqual(response.json().keys()[0], 'short_url')
        self.assertEqual(
            response.json()['short_url'],
            'http://%s/%s' % (SERVER_NAME, coursera_link.code))

    def test_redirect(self):
        """
        Navigating to a shortened link
        """
        qty = self.google_link.qty
        response = self.client.get(
            '/%s' % self.google_link.code)
        self.assertEqual(response.url, self.google_link.url)
        google_link = Link.objects.get(url=self.google_link.url)
        self.assertEqual(qty + 1, google_link.qty)
