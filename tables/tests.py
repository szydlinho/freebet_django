from django.urls import reverse
from django.test import TestCase
from django.urls import resolve
from .views import matches_list_view_base

class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, matches_list_view_base)